from base import TBase
from configparser import ConfigParser

import loader

class LOADER_T (TBase):

    def testLoader (t):
        obj = None
        fn = './data/s0/t0.ini'
        with open (fn, 'r') as fh:
            p = ConfigParser ()
            p.read_file (fh)
            obj = loader.load (fn, p)
            fh.close ()
        t.assertIsNotNone (obj)
