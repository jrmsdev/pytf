from unittest import TestCase
from io import StringIO

import cmd

class CMD_T (TestCase):

    def testMain (t):
        # run main
        s = StringIO ()
        t.assertEqual (cmd.main (stream = s, srcdir = './data/s0'), 0)
        # check main output
        s.seek (0, 0)
        with open ('./data/s0.out', 'r') as fh:
            t.assertEqual (len (s.read ()), len (fh.read ()))
            fh.close ()
