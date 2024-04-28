from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import TeacherProfile


@receiver(post_save, sender=get_user_model())
def create_teacher_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == 1:
        TeacherProfile.objects.create(user=instance)
