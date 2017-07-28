from base import TBase
from unittest.mock import MagicMock

class MockResponse (object):
    status = 200

class TC_HTTP_T (TBase):

    def testHTTP (t):
        from tc_http import TC_HTTP
        k = TC_HTTP ('filename', 'tname')
        k.doRequest = MagicMock (return_value = MockResponse ())
        k.runTest ()
        k.doRequest.assert_called ()
        t.assertEqual (k.doRequest.called, 1)
