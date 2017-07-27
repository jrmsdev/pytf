from tc_base import TC_BASE

class TC_HTTP (TC_BASE):
    enable = True
    port = 80
    ssl = False
    uri = None

    def validate (t, d):
        t.enable = bool (d.get ('enable', t.enable))
        t.port = int (d.get ('port', t.port))
        t.ssl = bool (d.get ('ssl', t.ssl))
        t.uri = str (d.get ('uri', t.uri))

    def runTest (t):
        pass
