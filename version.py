VMAJOR = 0
VMINOR = 1
VPATCH = 0

def getString ():
    v = '{}.{}'.format (VMAJOR, VMINOR)
    if VPATCH > 0:
        v = '{}.{}'.format (v, VPATCH)
    return v
