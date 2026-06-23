from repohealth.code_metrics import count_lines


def test_count_lines_existing_file(tmp_path):
    file_path = tmp_path / "example.py"
    file_path.write_text("print('a')\nprint('b')\n")

    assert count_lines(str(file_path)) == 2


def test_count_lines_missing_file(tmp_path):
    file_path = tmp_path / "missing.py"

    assert count_lines(str(file_path)) == 0