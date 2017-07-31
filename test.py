#!/usr/bin/env python3

from unittest import TestLoader

ldr = TestLoader()
suite = ldr.discover('test', '*_t.py')

if __name__ == '__main__':

    import sys
    from unittest import TextTestRunner
    import version

    print ('tf v{}'.format (version.getString ()))

    verbose = 1
    if '-v' in sys.argv:
        verbose = 2

    rnr = TextTestRunner(verbosity=verbose)
    rst = rnr.run(suite)

    sys.exit(len(rst.errors))
