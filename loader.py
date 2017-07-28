import tc_http

TCMAP = {
    'http': tc_http.TC_HTTP,
}

def load (filename, cfg):

    def loadAttribs (sec, obj):
        d = dict ()
        for optn, optv in cfg.items (sec):
            if hasattr (obj, optn):
                d[optn] = optv
            else:
                raise RuntimeError ('invalid test class option: ' + optn)
        obj.validate (d)
        return obj

    for sec in cfg.sections ():
        n = sec.split (':')[0].strip ()
        k = TCMAP.get (n, None)
        if k is None:
            raise RuntimeError ('invalid test class: ' + n)
        else:
            yield loadAttribs (sec, k (filename, sec))
