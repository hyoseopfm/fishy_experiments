################################################################################
# About
################################################################################

"""Entrypoint to the hello program."""

################################################################################
# Imports
################################################################################

import emoji

from . import starfish

################################################################################
# Entrypoint
################################################################################


def main() -> None:
    print(emoji.emojize('Python is :thumbs_up:'))
    print(emoji.emojize('Hello, something is :fish:'))
    print("Hello, something's fishy...")
    print(f"Hello, I am {starfish.bluey()}")
