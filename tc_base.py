from unittest import TestCase
from os.path import dirname, basename, join

class TC_BASE (TestCase):
    filename = None
    name = None

    def __init__ (t, filename, name):
        t.filename = join (basename (dirname (filename)), basename (filename))
        t.name = name
        super (TC_BASE, t).__init__ ()

    def __str__ (t):
        return ' '.join ([t.filename, t.name])
