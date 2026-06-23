from pathlib import Path

from repohealth.git_utils import create_temp_dir


def test_create_temp_dir_creates_directory():
    temp_dir = create_temp_dir()

    assert Path(temp_dir).exists()