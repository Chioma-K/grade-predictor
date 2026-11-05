
def calculate_final_grade(assignment: float, midterm: float, final_exam: float) -> float | str:
    """Calculates the final grade based on the assignment, midterm, and final exam scores.
    The final grade is calculated as follows:
    - Assignment: 20%
    - Midterm: 40%
    - Final Exam: 40%
    Returns the final grade as a float if all scores are valid, otherwise returns an error message as a string."""
    scores = [assignment, midterm, final_exam]
    
    for score in scores:
        if not (0 <= score <= 100):
            return "Invalid score. Please enter a score between 0 and 100."
        
    return assignment * 0.20 + midterm * 0.40 + final_exam * 0.40