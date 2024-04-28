from django.apps import AppConfig

class GetCourseConfig(AppConfig):
    name = 'GetCourse'

    def ready(self):
        import GetCourse.signals
