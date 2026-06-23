from repohealth.metrics import is_bugfix_commit


def test_is_bugfix_commit_without_bug_keyword():
    assert is_bugfix_commit("add new feature") is False