import pytest

from settings.app import AppSettings
from os import environ


@pytest.fixture
def environment_settings():
    old_env = environ.get("ENV")
    environ["ENV"] = "blah!"
    yield
    if old_env is not None:
        environ["ENV"] = old_env
    else:
        environ.pop("ENV")


class TestAppConfig:
    @pytest.mark.usefixtures("environment_settings")
    def test_env_from_env_variable(self):
        settings = AppSettings()
        assert settings.environment == "blah!"

    def test_env_from_file(self):
        settings = AppSettings()
        assert settings.environment
