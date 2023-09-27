from django.contrib import admin
from django.contrib.admin import display

from academy.models import *


class FinancialLiteracyAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'financial_literacy')


class AdviceRequestsAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'advice_requests', 'phone_number')


class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'active', 'default_course', 'teacher')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')


class MyCoursesListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_title', 'added_date', 'teacher')

    @display(ordering='courses__title', description='course_title')
    def get_title(self, obj):
        return obj.courses.title


class QuestionAdmin(admin.ModelAdmin):

    def exam_and_position(obj):
        return "%s ,question %s" % (obj.exam, obj.position)

    list_display = (exam_and_position,)


class ResponseExamAdmin(admin.ModelAdmin):
    list_display = ['question', 'exam_id', 'answer']


class CorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'exam_id', 'answer']


class VideoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_title')

    @display(ordering='course__title', description='course_title')
    def get_title(self, obj):
        return obj.course.title


class ExamsAdmin(admin.ModelAdmin):
    def course_and_position(obj):
        return "%s exam %s" % (obj.course, obj.position)

    list_display = (course_and_position,)


admin.site.register(FinancialLiteracy, FinancialLiteracyAdmin)
admin.site.register(AdviceRequests, AdviceRequestsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(MyCoursesList, MyCoursesListAdmin)
admin.site.register(Exams, ExamsAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(CorrectAnswer, CorrectAnswerAdmin)
admin.site.register(ResponseExam, ResponseExamAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Video, VideoListAdmin)
