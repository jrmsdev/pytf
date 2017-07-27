from configparser import ConfigParser
from unittest.suite import TestSuite
from glob import glob
from os import path

import tc

def load (src):
    s = TestSuite ()

    def scanDir (d):
        l = []
        for f in glob (path.join (d, '*.ini')):
            l.append (f)
        return sorted (l)

    for f in scanDir (src):
        with open (f, 'r') as fh:
            p = ConfigParser ()
            p.read_file (fh)
            for t in tc.load (f, p):
                s.addTest (t)
            fh.close ()

    return s
