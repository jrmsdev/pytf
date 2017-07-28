from tc import TC_BASE
from urllib.request import urlopen

class TC_HTTP (TC_BASE):
    enable = True
    ssl = False
    uri = None
    post = None
    timeout = 10
    status = 200

    def validate (t, d):
        t.enable = bool (d.get ('enable', t.enable))
        t.ssl = bool (d.get ('ssl', t.ssl))
        t.uri = d.get ('uri', t.uri)
        t.post = d.get ('post', t.post)
        t.timeout = int (d.get ('timeout', t.timeout))

    def doRequest (t):
        return urlopen (t.uri, t.post, t.timeout)

    def runTest (t):
        resp = t.doRequest ()
        t.assertEqual (resp.status, t.status)
