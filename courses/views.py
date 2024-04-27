from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, Enrollment


@login_required
def create_course(request):
    if request.user.user_type != 1:
        return redirect('home')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'courses/create_course.html', {'form': form})


def course_list(request):
    courses = Course.objects.filter(available=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, available=True)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('/')
