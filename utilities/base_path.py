from pathlib import Path


def get_base_path() -> Path:
    return Path(__file__).parent.parent.absolute()


def get_env_path() -> Path:
    return get_base_path() / "env"
