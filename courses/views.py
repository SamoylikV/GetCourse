from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Course, Enrollment, PDFFile
from .forms import CourseForm, PDFFileForm
from django.forms import modelformset_factory


@login_required
def create_course(request):
    PDFFileFormSet = modelformset_factory(PDFFile, form=PDFFileForm, extra=1)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        formset = PDFFileFormSet(request.POST, request.FILES, queryset=PDFFile.objects.none())
        if form.is_valid() and formset.is_valid():
            course = form.save()
            for form in formset.cleaned_data:
                if form:
                    pdf = form['file']
                    pdf_file = PDFFile(file=pdf)
                    pdf_file.save()
                    course.pdf_files.add(pdf_file)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()
        formset = PDFFileFormSet(queryset=PDFFile.objects.none())
    return render(request, 'courses/create_course.html', {'form': form, 'formset': formset})


def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def course_list(request):
    courses = Course.objects.filter(available=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, available=True)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('/')
