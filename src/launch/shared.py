import ctypes as lib
import sys

libc = None

if sys.platform in ("linux","darwin"):
    libc = lib.CDLL("libc.so.6")
else:
    ...
