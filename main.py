

def calculate_final_grade(assignment, midterm, final_exam):

    scores = [assignment, midterm, final_exam]

    for score in scores:
        if not (0 <= score <= 100):
            return "Invalid score. Please enter a score between 0 and 100."
        
    assignment *= 0.20
    midterm *= 0.40
    final_exam *= 0.40
    return assignment + midterm + final_exam


    
def main():
    grade = calculate_final_grade(90, 80, 95)
    print(grade)

    grade = calculate_final_grade(100, 100, 100)
    print(grade)

    grade = calculate_final_grade(200, 80, 95)
    print(grade)

    grade = calculate_final_grade(90, -5, 95)
    print(grade)

    grade = calculate_final_grade(0, 0, 0)
    print(grade)


if __name__ == "__main__":
    main()
