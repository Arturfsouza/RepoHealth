from repohealth.metrics import is_bugfix_commit


def test_is_bugfix_commit_without_bug_keyword():
    assert is_bugfix_commit("add new feature") is False


def test_is_bugfix_commit_with_fix_keyword():
    assert is_bugfix_commit("fix login error") is True


def test_is_bugfix_commit_with_bug_keyword():
    assert is_bugfix_commit("bug in payment service") is True