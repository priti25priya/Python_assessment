def calculate_average():

    student_marks = {
        'Hammy': [78, 90, 56],
        'Olivia': [91, 56, 78],
        'Yosh': [88, 79, 85]
    }

    student_name = input("Enter the student's name: ")


    if student_name in student_marks:
        marks = student_marks[student_name]
        average = sum(marks) / len(marks)
        return (f"{average:.2f}")




calculate_average()
