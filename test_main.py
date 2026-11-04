

from main import calculate_final_grade


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