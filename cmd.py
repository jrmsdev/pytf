from unittest.runner import TextTestRunner
import suite

def main (stream = None, srcdir = '.'):
    s = suite.load (src = srcdir)
    r = TextTestRunner (stream = stream, verbosity = 2).run (s)
    return len (r.errors) or len (r.failures)
