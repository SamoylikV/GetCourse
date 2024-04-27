from django.contrib import admin
from django.urls import path, include
from .views import student_dashboard, teacher_dashboard, register, CustomLoginView
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='course_list'), name='logout'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('', include('courses.urls')),
    path('courses/', include('courses.urls')),
    path('', RedirectView.as_view(url='/courses/', permanent=True)),

]
