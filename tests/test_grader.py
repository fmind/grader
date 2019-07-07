#!/usr/bin/env pytest

import grader


def test_generate_grade():
    grade = grader.generate_grade()

    assert 0 <= grade <= 20


def test_generate_grades():
    grades = grader.generate_grades()

    assert grades.keys() == {
        'biology',
        'english',
        'french',
        'maths',
        'music',
        'physics',
    }

    assert all(0 <= grade <= 20 for grade in grades.values())


def test_generate_student():
    student = grader.generate_student()

    assert student.keys() == {
        'academic_degree',
        'age',
        'full_name',
        'gender',
        'nationality',
        'university',
    }

    assert all(bool(x) for x in student.values())
