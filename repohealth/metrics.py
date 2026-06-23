def is_bugfix_commit(message: str) -> bool:
    if not message:
        return False

    message_lower = message.lower()
    keywords = ["fix", "bug", "error"]

    return any(keyword in message_lower for keyword in keywords)


def calculate_risk_score(
    commits: int,
    authors: int,
    bugfix_commits: int,
    lines: int = 0,
    complexity: int = 0
) -> int:
    if commits < 0 or authors < 0 or bugfix_commits < 0 or lines < 0 or complexity < 0:
        raise ValueError("As métricas não podem ser negativas.")

    return (
        (commits * 2)
        + (authors * 3)
        + (bugfix_commits * 4)
        + (lines // 50)
        + (complexity * 2)
    )

def classify_risk(score: int) -> str:
    if score < 0:
        raise ValueError("O score não pode ser negativo.")

    if score >= 50:
        return "Alto"

    if score >= 20:
        return "Médio"

    return "Baixo"