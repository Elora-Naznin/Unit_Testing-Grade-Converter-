def convert_to_letter_grade(grade):
    if not isinstance(grade, (int, float)):
        raise ValueError("Grade must be a number.")
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
