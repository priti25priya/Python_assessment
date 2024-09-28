def CalculateAverage():
    Students = [
        {"ID": 1, "Name": "Hammy", "Class": 12, "Marks": 90},
        {"ID": 2, "Name": "Olivia", "Class": 12, "Marks": 67},
        {"ID": 3, "Name": "Yosh", "Class": 12, "Marks": 98},
        {"ID": 4, "Name": "Priti", "Class": 12, "Marks": 88},
        {"ID": 5, "Name": "Dexter", "Class": 12, "Marks": 81},
    ]

    total_marks = 0
    numberofstudents = 0

    for i in Students:
        total_marks = total_marks + i["Marks"]
        numberofstudents += 1

    avg = (total_marks) / (numberofstudents)

    return avg