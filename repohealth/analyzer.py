from collections import defaultdict
from pathlib import Path

from pydriller import Repository


def analyze_repository(repo_path: str) -> list[dict]:
    if not repo_path:
        raise ValueError("O caminho do repositório não pode estar vazio.")

    if not Path(repo_path).exists():
        raise FileNotFoundError("O caminho informado não existe.")

    files_data = defaultdict(lambda: {
        "commits": 0,
        "authors": set(),
        "bugfix_commits": 0
    })

    for commit in Repository(repo_path).traverse_commits():
        for modified_file in commit.modified_files:
            file_path = modified_file.new_path or modified_file.old_path

            if not file_path:
                continue

            files_data[file_path]["commits"] += 1
            files_data[file_path]["authors"].add(commit.author.name)

    return []