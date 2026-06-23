import tempfile


def create_temp_dir() -> str:
    return tempfile.mkdtemp(prefix="repohealth_")