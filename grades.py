lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):
    """Returns an average of numbers in the list."""
    total = float(sum(numbers))
    average = total / len(numbers)
    return average


def get_average(student):
    """returns a weighted average for student."""
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])

    weighted_average = homework * .1 + quizzes * .3 + tests * .6
    return weighted_average


def get_letter_grade(score):
    """Makes number score into letter grade."""

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print get_letter_grade(lloyd)


def get_class_average(students):
    """Gets average grade of students."""
    results = []

    for student in students:
        results.append(get_average(student))

    return average(results)

print get_class_average([lloyd, alice, tyler])
print get_letter_grade(get_class_average([lloyd, alice, tyler]))
