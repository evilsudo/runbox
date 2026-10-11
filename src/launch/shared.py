import ctypes
from ctypes import util

libc_path = util.find_library("c")
libc = None
if libc_path:
    libc = ctypes.CDLL(libc_path)
else:
    raise ValueError("Oops! Runbox couldn't find a standard C library (required because this library isn't using anything except ctypes and sys) \n Please provide a path to the C library.")
