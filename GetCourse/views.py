from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm, TeacherProfileForm
from django.urls import reverse_lazy
from courses.models import Enrollment
from .models import TeacherProfile


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.user_type == 1:
            return reverse_lazy('teacher_dashboard')
        elif self.request.user.user_type == 2:
            return reverse_lazy('student_dashboard')
        else:
            return super().get_success_url()


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def student_dashboard(request):
    if request.user.user_type != 2:
        return redirect('home')
    enrollments = Enrollment.objects.filter(student=request.user)
    courses = [enrollment.course for enrollment in enrollments]
    return render(request, 'dashboards/student_dashboard.html', {'courses': courses})


@login_required
def teacher_dashboard(request):
    if request.user.user_type != 1:
        return redirect('/')
    return render(request, 'dashboards/teacher_dashboard.html')


def teachers_table(request):
    return render(request, 'community/teachers_table.html')


# @login_required
# def view_teacher_profile(request):
#     try:
#         profile = request.user.teacher_profile
#     except request.user._meta.model.teacher_profile.RelatedObjectDoesNotExist:
#         return redirect('edit_profile')
#     return render(request, 'profiles/teacher_profile.html', {'profile': profile})


@login_required
def view_teacher_profile(request, user_id=None):
    if user_id is None:
        user_id = request.user.id
    profile = get_object_or_404(TeacherProfile, user__id=user_id)

    return render(request, 'profiles/teacher_profile.html', {'profile': profile})


@login_required
def edit_teacher_profile(request):
    profile, created = TeacherProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = TeacherProfileForm(instance=profile)

    return render(request, 'profiles/edit_teacher_profile.html', {'form': form})


def list_teachers(request):
    teachers = TeacherProfile.objects.filter(user__user_type=1)
    return render(request, 'profiles/teachers_list.html', {'teachers': teachers})
