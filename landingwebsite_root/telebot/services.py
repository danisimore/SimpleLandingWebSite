from .models import TeleSettings


def get_settings():
    settings = TeleSettings.objects.get(pk=1)
    return settings
