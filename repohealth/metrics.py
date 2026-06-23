def is_bugfix_commit(message: str) -> bool:
    if not message:
        return False

    message_lower = message.lower()

    return "fix" in message_lower or "bug" in message_lower