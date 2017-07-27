from unittest import TestCase
from configparser import ConfigParser

import tc

class TC_T (TestCase):

    def testLoad (t):
        obj = None
        fn = './data/s0/t0.ini'
        with open (fn, 'r') as fh:
            p = ConfigParser ()
            p.read_file (fh)
            obj = tc.load (fn, p)
            fh.close ()
        t.assertIsNotNone (obj)
