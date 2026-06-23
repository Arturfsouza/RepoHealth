from collections import defaultdict
from pathlib import Path

from pydriller import Repository
from repohealth.code_metrics import calculate_complexity, count_lines
from repohealth.metrics import calculate_risk_score, classify_risk, is_bugfix_commit


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
        commit_is_bugfix = is_bugfix_commit(commit.msg)

        for modified_file in commit.modified_files:
            file_path = modified_file.new_path or modified_file.old_path

            if not file_path:
                continue

            files_data[file_path]["commits"] += 1
            files_data[file_path]["authors"].add(commit.author.name)

            if commit_is_bugfix:
                files_data[file_path]["bugfix_commits"] += 1

    result = []

    for file_path, data in files_data.items():
        authors_count = len(data["authors"])
        absolute_file_path = Path(repo_path) / file_path
        lines = count_lines(str(absolute_file_path))
        complexity = calculate_complexity(str(absolute_file_path))

        score = calculate_risk_score(
            commits=data["commits"],
            authors=authors_count,
            bugfix_commits=data["bugfix_commits"],
            lines=lines,
            complexity=complexity
        )

        result.append({
            "file": file_path,
            "commits": data["commits"],
            "authors": authors_count,
            "bugfix_commits": data["bugfix_commits"],
            "lines": lines,
            "complexity": complexity,
            "score": score,
            "risk": classify_risk(score)
        })

    return sorted(result, key=lambda item: item["score"], reverse=True)