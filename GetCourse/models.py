from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'teacher'),
        (2, 'student'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)


class TeacherProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='teacher_profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.user.username


class StudentProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    interests = models.ManyToManyField('courses.Course', related_name='interested_students')

    def __str__(self):
        return self.user.username
