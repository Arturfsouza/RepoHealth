def is_bugfix_commit(message: str) -> bool:
    if not message:
        return False

    return "fix" in message.lower()