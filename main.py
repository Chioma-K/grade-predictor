from grades import calculate_final_grade

def get_scores() -> list[float] | None:
    """Prompt the user for scores and convert them to floats. 
    Return a list of floats if conversion succeeds, or None if it fails.
    """

    input_scores = input("Enter the scores for assignment, midterm, and final exam separated by spaces: ")
    
    try:
        scores = list(map(float, input_scores.split()))
    except ValueError:
        print("Please enter numeric scores.")
        return
    
    return scores
    
    
def main() -> None:
    """Main function to run the grade calculation program."""

    scores = get_scores()
    
    if scores is None:
        return

    if len(scores) != 3:
        print("Please enter exactly three scores.")
        return
    
    grade = calculate_final_grade(*scores)
    print(grade)



if __name__ == "__main__":
    main()
