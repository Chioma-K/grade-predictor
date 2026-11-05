

def calculate_final_grade(assignment, midterm, final_exam):

    scores = [assignment, midterm, final_exam]
    

    for score in scores:
        if not (0 <= score <= 100):
            return "Invalid score. Please enter a score between 0 and 100."
        
    return assignment * 0.20 + midterm * 0.40 + final_exam * 0.40


    
def main():
    input_scores = input("Enter the scores for assignment, midterm, and final exam separated by spaces: ")
    
    try:
        scores = list(map(float, input_scores.split()))
    except ValueError:
        print("Please enter numeric scores.")
        return 
    
    if len(scores) != 3:
        print("Please enter exactly three scores.")
        return
    grade = calculate_final_grade(*scores)
    print(grade)



if __name__ == "__main__":
    main()
