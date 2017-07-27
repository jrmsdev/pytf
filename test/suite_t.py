from unittest import TestCase

import suite

class SUITE_T (TestCase):

    def testLoad (t):
        s = suite.load (src = './data/s0')
        t.assertEqual (len (s._tests), 2)
