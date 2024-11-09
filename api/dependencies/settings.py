from settings.app import AppSettings


def get_app_settings() -> AppSettings:
    return AppSettings()


__all__ = ["get_app_settings"]
