def is_bugfix_commit(message: str) -> bool:
    if not message:
        return False

    message_lower = message.lower()

    return "fix" in message_lower or "bug" in message_lower


def calculate_risk_score(commits: int, authors: int, bugfix_commits: int) -> int:
    return (commits * 2) + (authors * 3) + (bugfix_commits * 4)