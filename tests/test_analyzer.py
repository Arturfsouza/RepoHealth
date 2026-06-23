from repohealth.analyzer import analyze_repository


def test_analyze_repository_returns_list_for_basic_call(tmp_path):
    result = analyze_repository(str(tmp_path))

    assert isinstance(result, list)