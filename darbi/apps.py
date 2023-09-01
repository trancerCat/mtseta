from django.apps import AppConfig
from .services import ProjectManagment


class DarbiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'darbi'

    def ready(self):
        self.project_managment = ProjectManagment()
