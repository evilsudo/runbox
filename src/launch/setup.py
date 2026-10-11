"""File to set up launching of the program."""
from .shared import libc


def _launch(path: str):
    libc.fork()
    # (To make sure python doesn't suicide itself when launching programs)
