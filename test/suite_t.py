from base import TBase

import suite

class SUITE_T (TBase):

    def testSuiteLoad (t):
        s = suite.load (src = './data/s0')
        t.assertEqual (len (s._tests), 2)
        t.assertEqual (str (s._tests[0]), 's0/t0 http:0')
        t.assertEqual (str (s._tests[1]), 's0/t0 http:1')
