"""Generators of the project."""

from mimesis import Person  # type: ignore
from numpy.random import normal  # type: ignore


def generate_grade(mean: float = 10.0, std: float = 3.0) -> float:
    """Generate a grade from a normal distribution."""
    grade = normal(mean, std)

    if grade < 0:
        grade = 0
    elif grade > 20:
        grade = 20

    return grade


def generate_grades() -> dict:
    """Generate a set of grades record."""
    grades = {
        "biology": generate_grade(10, 3.5),
        "english": generate_grade(15, 2),
        "french": generate_grade(9, 4),
        "maths": generate_grade(8, 5),
        "music": generate_grade(12, 3),
        "physics": generate_grade(13, 1.5),
    }

    return grades


def generate_student() -> dict:
    """Generate a student record."""
    person = Person()

    student = {
        "academic_degree": person.academic_degree(),
        "age": person.age(),
        "full_name": person.full_name(),
        "gender": person.gender(),
        "nationality": person.nationality(),
        "university": person.university(),
    }

    return student
