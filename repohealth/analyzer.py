from pathlib import Path


def analyze_repository(repo_path: str) -> list[dict]:
    if not repo_path:
        raise ValueError("O caminho do repositório não pode estar vazio.")

    if not Path(repo_path).exists():
        raise FileNotFoundError("O caminho informado não existe.")

    return []