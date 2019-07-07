#!/usr/bin/env python3

"""Generate a list of student and grade records."""

import argparse
import json

import grader

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument("-n", type=int, default=1000, help="records to generate")


def main(args=None):
    """Entry point of the script."""
    opts = PARSER.parse_args(args)

    for _ in range(0, opts.n):
        student = grader.generate_student()
        grades = grader.generate_grades()
        record = {**student, **grades}

        print(json.dumps(record))


if __name__ == "__main__":
    main()
