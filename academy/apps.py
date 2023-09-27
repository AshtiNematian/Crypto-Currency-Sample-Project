from django.apps import AppConfig


class AcademyConfig(AppConfig):
    name = 'academy'

    def ready(self):
        import academy.signals
