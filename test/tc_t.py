from base import TBase
from tc import TC_BASE

class TC_T (TBase):

    def testTCBase (t):
        k = TC_BASE ('filename', 'tname')
        t.assertEqual (str (k), 'filename tname')
