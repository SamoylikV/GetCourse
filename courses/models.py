from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
