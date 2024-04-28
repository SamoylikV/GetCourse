from django.contrib import admin
from django.urls import path, include
from .views import student_dashboard, teacher_dashboard, register, CustomLoginView, edit_teacher_profile, \
    view_teacher_profile, list_teachers
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='course_list'), name='logout'),
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    path('teacher-dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('edit-profile/', edit_teacher_profile, name='edit_profile'),
    # path('profile/', view_teacher_profile, name='profile_view'),
    path('profile/', view_teacher_profile, name='profile_view'),
    path('profile/<int:user_id>/', view_teacher_profile, name='profile_view'),
    path('profiles/', list_teachers, name='teachers_list'),
    path('', include('courses.urls')),
    path('courses/', include('courses.urls')),
    path('', RedirectView.as_view(url='/courses/', permanent=True)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
