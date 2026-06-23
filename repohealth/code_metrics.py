from pathlib import Path

import lizard


def count_lines(file_path: str) -> int:
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return 0

    try:
        with path.open("r", encoding="utf-8", errors="ignore") as file:
            return sum(1 for _ in file)
    except OSError:
        return 0


def calculate_complexity(file_path: str) -> int:
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return 0

    try:
        analysis = lizard.analyze_file(str(path))
        return sum(function.cyclomatic_complexity for function in analysis.function_list)
    except Exception:
        return 0