from repohealth.code_metrics import calculate_complexity, count_lines


def test_count_lines_existing_file(tmp_path):
    file_path = tmp_path / "example.py"
    file_path.write_text("print('a')\nprint('b')\n")

    assert count_lines(str(file_path)) == 2


def test_count_lines_missing_file(tmp_path):
    file_path = tmp_path / "missing.py"

    assert count_lines(str(file_path)) == 0

def test_calculate_complexity_existing_file(tmp_path):
    file_path = tmp_path / "example.py"
    file_path.write_text(
        "def example(x):\n"
        "    if x > 0:\n"
        "        return x\n"
        "    return 0\n"
    )

    assert calculate_complexity(str(file_path)) > 0


def test_calculate_complexity_missing_file(tmp_path):
    file_path = tmp_path / "missing.py"

    assert calculate_complexity(str(file_path)) == 0