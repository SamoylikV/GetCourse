# Generated by Django 5.0.4 on 2024-05-01 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='keywords',
            field=models.TextField(default=''),
        ),
    ]
