from pathlib import Path

import pytest

from repohealth.git_utils import clone_repository, create_temp_dir, is_git_repository


def test_create_temp_dir_creates_directory():
    temp_dir = create_temp_dir()

    assert Path(temp_dir).exists()


def test_clone_repository_with_empty_url(tmp_path):
    with pytest.raises(ValueError):
        clone_repository("", str(tmp_path))

def test_clone_repository_with_empty_destination():
    with pytest.raises(ValueError):
        clone_repository("https://github.com/example/repo.git", "")

def test_is_git_repository_false_for_normal_folder(tmp_path):
    assert is_git_repository(str(tmp_path)) is False

def test_is_git_repository_true_when_git_folder_exists(tmp_path):
    git_folder = tmp_path / ".git"
    git_folder.mkdir()

    assert is_git_repository(str(tmp_path)) is True