from pathlib import Path

import pytest

from repohealth.git_utils import clone_repository, create_temp_dir


def test_create_temp_dir_creates_directory():
    temp_dir = create_temp_dir()

    assert Path(temp_dir).exists()


def test_clone_repository_with_empty_url(tmp_path):
    with pytest.raises(ValueError):
        clone_repository("", str(tmp_path))