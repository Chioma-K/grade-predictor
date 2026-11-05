
from unittest.mock import patch
from main import main, calculate_final_grade


def test_calculate_final_grade():
    assert calculate_final_grade(90, 80, 95) == 88.0

def test_calculate_final_grade_edge_cases():
    assert calculate_final_grade(100, 100, 100) == 100.0

def test_calculate_final_grade_invalid_scores():
    assert calculate_final_grade(200, 80, 95) == "Invalid score. Please enter a score between 0 and 100."

def test_calculate_final_grade_negative_scores():
    assert calculate_final_grade(90, -5, 95) == "Invalid score. Please enter a score between 0 and 100."

def test_calculate_final_grade_zero_scores():
    assert calculate_final_grade(0, 0, 0) == 0.0

def test_main_valid_input(capsys):
    with patch("builtins.input", return_value="90 80 95"):
        main()

    captured = capsys.readouterr()
    assert captured.out == "88.0\n"

def test_main_non_numeric_input(capsys):
    with patch("builtins.input", return_value="90 hello 95"):
        main()

    captured = capsys.readouterr()
    assert captured.out == "Please enter numeric scores.\n"

def test_main_missing_score(capsys):
    with patch("builtins.input", return_value="90 80"):
        main()

    captured = capsys.readouterr()
    assert captured.out == "Please enter exactly three scores.\n"

def test_main_extra_score(capsys):
    with patch("builtins.input", return_value="90 80 95 70"):
        main()

    captured = capsys.readouterr()
    assert captured.out == "Please enter exactly three scores.\n"

def test_main_out_of_range(capsys):
    with patch("builtins.input", return_value="150 80 95"):
        main()

    captured = capsys.readouterr()
    assert captured.out == "Invalid score. Please enter a score between 0 and 100.\n"