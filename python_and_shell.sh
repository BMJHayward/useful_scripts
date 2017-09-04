#!/bin/sh

"""":
if which python >/dev/null; then
    exec python "$0" "$@"
else
    echo "${0##*/}: Python not found. Please install Python." >&2
    exit 1
fi
"""

__doc__ = """
Leading 4x" in line 3 allow you to mix Python + shell script.
"""

import sys
print "Hello World!"
print "Python version: ", sys.version
print "Arg vector: ", sys.argv
print "This is the doc: ", __doc__
sys.exit (0)