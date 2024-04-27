from django.urls import path
from .views import course_list, create_course

urlpatterns = [
    path('courses/', course_list, name='course_list'),
    path('courses/create/', create_course, name='create_course'),
]