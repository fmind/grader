#!/usr/bin/env python3

"""Entry point of the project."""

import argparse

PARSER = argparse.ArgumentParser(description=__doc__)


def main(args=None):
    """Entry point of the script."""
    opts = PARSER.parse_args(args)

    print(opts)


if __name__ == "__main__":
    main()
