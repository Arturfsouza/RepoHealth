import tempfile

from git import Repo


def create_temp_dir() -> str:
    return tempfile.mkdtemp(prefix="repohealth_")


def clone_repository(repo_url: str, destination: str) -> str:
    if not repo_url:
        raise ValueError("A URL do repositório não pode estar vazia.")

    Repo.clone_from(repo_url, destination)

    return destination