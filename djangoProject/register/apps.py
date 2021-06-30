"""Apps python file"""

# pylint: disable = E0401
from django.apps import AppConfig


# pylint: disable = R0903
class RegisterConfig(AppConfig):
    """
    register config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'register'
