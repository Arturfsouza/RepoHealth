from repohealth.metrics import calculate_risk_score, is_bugfix_commit

def test_is_bugfix_commit_without_bug_keyword():
    assert is_bugfix_commit("add new feature") is False


def test_is_bugfix_commit_with_fix_keyword():
    assert is_bugfix_commit("fix login error") is True


def test_is_bugfix_commit_with_bug_keyword():
    assert is_bugfix_commit("bug in payment service") is True

def test_is_bugfix_commit_with_empty_message():
    assert is_bugfix_commit("") is False

def test_calculate_risk_score():
    assert calculate_risk_score(commits=10, authors=2, bugfix_commits=3) == 38

def test_calculate_risk_score_with_zero_values():
    assert calculate_risk_score(commits=0, authors=0, bugfix_commits=0) == 0