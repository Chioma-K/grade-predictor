# Grade Predictor

A Python application that calculates a student's final grade using weighted assignment, midterm, and final examination scores.

## Features

- Calculates final grades using weighted scores.
- Validates that each score is between 0 and 100.
- Returns a descriptive message for invalid inputs.
- Includes automated tests using pytest.

## Grade Calculation

The final grade is calculated using the following weights:

| Assessment | Weight |
|---|---:|
| Assignment | 20% |
| Midterm | 40% |
| Final Examination | 40% |

**Formula:**

Final Grade = (Assignment × 0.20) + (Midterm × 0.40) + (Final Exam × 0.40)

## Technologies

- Python
- pytest
- uv
- Git and GitHub

## Getting Started

### Prerequisites

Install Python and [uv](https://docs.astral.sh/uv/).

### Installation

Clone the repository:

```bash
git clone https://github.com/Chioma-K/grade-predictor.git
cd grade-predictor
```

Install the project dependencies:

```bash
uv sync
```

### Run the Application

```bash
uv run main.py
```

### Run Automated Tests

```bash
uv run pytest -v
```

## Example

**Input:**

- Assignment: 90
- Midterm: 80
- Final Examination: 95

**Output:**

```text
88.0
```

## Testing

The project includes five automated tests covering:

1. Valid grade calculation.
2. Perfect scores.
3. Scores above the allowed maximum.
4. Negative scores.
5. Zero scores.

## Future Improvements

- Accept scores interactively from users.
- Convert numerical grades into letter grades.
- Improve error handling.
- Build a simple user interface.

## Author

Chioma K.

## Project Status

Beginner Python software engineering project focused on functions, validation, automated testing, and version control.
