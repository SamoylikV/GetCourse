from django.urls import path
from .views import course_list, enroll_course, create_course, course_detail

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('create/', create_course, name='create_course'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('create/', create_course, name='create_course'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
]