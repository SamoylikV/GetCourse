from django import forms
from .models import Course, PDFFile


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'max_participants', 'pdf_files', 'available']


class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['file']
