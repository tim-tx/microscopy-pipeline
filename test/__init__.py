import sys

if not (sys.version_info.major == 3):
    raise ImportError("microscopy-pipeline requires Python 3")

del sys
