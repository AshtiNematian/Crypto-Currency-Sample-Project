from django.http import FileResponse
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import User

from academy.serializers import *


class CoursesDetailsView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class TeacherDetailsView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class AllCoursesView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class DefaultCoursesListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Courses.objects.filter(default_course=True)
    serializer_class = CoursesSerializer


class FinancialLiteracyView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = FinancialLiteracySerializer

    def get_queryset(self, **kwargs):
        user = self.request.user
        financial_lit = FinancialLiteracy.objects.get(user_financial_literacy=user)
        if not financial_lit:
            financial_literacy = kwargs.pop('financial_literacy', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, user=user, financial_literacy=financial_literacy)
            serializer.is_valid(raise_exception=True)
            serializer.create(serializer.data)
            serializer.save()


class FinancialLiteracyActivesView(viewsets.ViewSet):
    serializer_class = FinancialLiteracySerializer

    def list(self, request):
        user = self.request.user
        queryset = AdviceRequests.objects.get(user=user)
        serializer = FinancialLiteracySerializer(queryset)
        active = serializer.data['active']
        return Response(active)


class AdviceRequestsView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = AdviceRequestsSerializer

    def get_queryset(self, **kwargs):
        user = self.request.user
        advice_req = AdviceRequests.objects.get(user=user)

        if user:
            if not advice_req.active:
                advice_requests = kwargs.pop('advice_requests', False)
                phone_number = kwargs.pop('phone_number', False)
                instance = self.get_object()

                serializer = self.get_serializer(instance, user=user, advice_requests=advice_requests,
                                                 phone_number=phone_number)
                serializer.is_valid(raise_exception=True)
                serializer.create(serializer.data)
                serializer.save()
                advice_req.activate = True
                advice_req.save()
            raise exceptions.AuthenticationFailed()


class AdviceRequestActivesView(viewsets.ViewSet):
    serializer_class = AdviceRequestsSerializer

    def list(self, request):
        user = self.request.user
        queryset = AdviceRequests.objects.get(user=user)
        serializer = AdviceRequestsSerializer(queryset)
        active = serializer.data['active']
        return Response(active)


class AdviceCoursesListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = CoursesSerializer

    def get_queryset(self, **kwargs):
        user = self.request.user
        courses = Courses.objects.filter(user_courses=user.pk)
        return courses


class MyCoursesListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = MyCoursesListSerializer

    def get_queryset(self, **kwargs):
        user = self.request.user
        courses = MyCoursesList.objects.filter(user=user.pk)
        print(courses)
        return courses


class AddtoMyCoursesView(viewsets.GenericViewSet):
    serializer_class = MyCoursesListSerializer

    def create(self, *args, **kwargs):
        pk = self.request.POST.get('pk')
        print(pk)
        user = self.request.user.id
        print(user)

        if MyCoursesList.objects.filter(pk=pk, user=user).exists():
            return Response("Item already exists", status.HTTP_400_BAD_REQUEST)


# __________________________________________ View of Questions ___________________________________

class QuestionExamsView(viewsets.GenericViewSet):
    # permission_classes = (permissions.AllowAny,)

    @action(methods=['GET'], detail=True, url_name='questions', url_path='questions')
    def get_questions(self, request, pk=None):
        queryset = Exams.objects.all()
        exam = get_object_or_404(queryset, pk=pk)
        questions = Questions.objects.filter(exam=exam)

        serializer_questions = QuestionSerializer(instance=questions, many=True)
        return Response(serializer_questions.data, status=status.HTTP_200_OK)


# __________________________________ Response Exma( get result of exam ) _________________________


class ResponseExamView(GenericViewSet):
    permission_classes = [IsAuthenticated, ]

    @action(methods=['GET'], detail=True, url_name='response', url_path='response')
    def response(self, request, pk=None):

        response_exam = ResponseExam.objects.filter(exam=pk).filter(user=self.request.user)
        queryset_answer = CorrectAnswer.objects.filter(exam=pk)
        all_score = len(queryset_answer) * 10
        sum_score = 0
        list_question_id = [sub['question_id'] for sub in queryset_answer.values()]

        for i in list_question_id:

            question_id = i
            if response_exam.filter(question=question_id).values()[0]['answer'] == \
                    queryset_answer.filter(question=question_id).values()[0]['answer']:

                ResponseExam.objects.filter(question=question_id).filter(user=self.request.user).update(score=10)
                sum_score += 10
            else:
                ResponseExam.objects.filter(question=question_id).filter(user=self.request.user).update(score=0)

        final_score = f'{sum_score} from {all_score}'
        percentage_score = round((sum_score / all_score) * 100, 2)
        if percentage_score >= 60:
            result = 'accepted'
        else:
            result = 'rejected'
        response = ResponseExam.objects.filter(exam=pk).filter(user=self.request.user)
        ser_response = ResponseExamSerializer(response, many=True)
        return Response(
            data={'response': ser_response.data, 'final_score': final_score, 'percentage_score': percentage_score,
                  'result': result},
            status=status.HTTP_200_OK)


# ___________________________________________ Take Exam ________________________________________
class TakeExamApiView(GenericViewSet):
    permission_classes = [IsAuthenticated, ]

    @action(methods=['POST'], detail=True, url_name='answer', url_path='answer')
    def answer(self, request, pk=None):
        user_id = request.user.pk
        user = User.objects.get(id=user_id)

        exam_id = Exams.objects.get(id=pk)

        dict_position = dict(request.data)['position']
        dict_answer = dict(request.data)['answer']

        for i in range(0, len(dict_position)):
            position = get_object_or_404(Questions.objects.filter(exam=pk), position=dict_position[i])

            response = ResponseExam.objects.create(user=user, exam=exam_id, question=position,
                                                   answer=dict_answer[i])
            response.save()
        response_exam = ResponseExam.objects.filter(user=user, exam=exam_id)
        serializer_response = ResponseExamSerializer(instance=response_exam, many=True)
        return Response(serializer_response.data, status=status.HTTP_200_OK)


# _________________________________________________________________________________________________
class VideoDownloadView(viewsets.ModelViewSet):
    queryset = Video.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VideoSerializer

    @action(detail=True, methods=['get'], name='Videos_download')
    def download(self, request, pk):
        video = self.get_object()
        file_handle = video.video_file.open()
        return FileResponse(file_handle, 'r')


class VideoListView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


# _______________________________ get exam id from course_id _____________________________________


class ExamIdApiView(viewsets.GenericViewSet):
    serializer_class = CoursesSerializer

    @action(methods=['GET'], detail=True, url_name='id', url_path='id')
    def get_id(self, request, pk=None):
        queryset = Exams.objects.filter(course_id=pk)
        ser_data = ExamsSerializer(instance=queryset, many=True)
        list_id_exam = []
        for i in range(0, len(queryset)):
            list_id_exam.append(ser_data.data[i]['questions'][0]['exam'])

        return Response(list_id_exam)
