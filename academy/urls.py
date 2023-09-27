from rest_framework.routers import DefaultRouter
from django.urls import include, path

from academy.views import *


router = DefaultRouter()
router.register("course_detail", CoursesDetailsView, basename="course_detail")
router.register("teacher_detail", TeacherDetailsView, basename="teacher_detail")
router.register("my_course_list", MyCoursesListView, basename="my_course_list")
router.register("default_course_view", DefaultCoursesListView, basename="default_course_view")
router.register("all_course_view", AllCoursesView, basename="all_course_view")
router.register("add_to_my_course", AddtoMyCoursesView, basename="add_to_my_course")
router.register("financial_literacy", FinancialLiteracyView, basename="financial_literacy")
router.register("Active_financial_literacy", FinancialLiteracyActivesView, basename="Active_financial_literacy")
router.register("advice_requests", AdviceRequestsView, basename="advice_requests")
router.register("active_advice_requests", AdviceRequestActivesView, basename="active_advice_requests")
router.register("display-questions", QuestionExamsView, basename="display_questions")
router.register("display_response", ResponseExamView, basename="display_response")
router.register("video_download", VideoDownloadView, basename="video_download")
router.register("video_list", VideoListView, basename="video_list")
router.register("exam_id", ExamIdApiView, basename="exam_id")
router.register("take_exam", TakeExamApiView, basename="take_exam")

urlpatterns = [
    path('', include(router.urls)),

]
