from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    max_participants = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    pdf_files = models.ManyToManyField('PDFFile', blank=True)

    def __str__(self):
        return self.title


class PDFFile(models.Model):
    file = models.FileField(upload_to='course_pdfs/')

    def __str__(self):
        return self.file.name


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrolled_students')
    date_enrolled = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f'{self.student.username} -> {self.course.title}'
