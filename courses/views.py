from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course


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
