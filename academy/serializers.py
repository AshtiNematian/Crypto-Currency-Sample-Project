from rest_framework import serializers
from academy.models import *


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'title', 'description', 'active', 'teacher']


class FinancialLiteracySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialLiteracy
        fields = ['id', 'user', 'financial_literacy']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class AdviceRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdviceRequests
        fields = ['id', 'user', 'advice_requests', 'phone_number', 'active']


class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdviceRequests
        fields = ['id', 'advice_requests', 'phone_number']


class MyCoursesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCoursesList
        fields = ['id', 'user', 'courses', 'added_date', 'teacher']


class ResponseExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseExam
        fields = '__all__'


class ExamsSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Exams
        fields = '__all__'

    def get_questions(self, obj):
        result = obj.question.all()
        return QuestionSerializer(instance=result, many=True).data


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'

    def get_questions(self, obj):
        result = obj.question.all()
        return QuestionSerializer(instance=result, many=True).data


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
