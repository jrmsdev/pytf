#!/usr/bin/env python3

import sys
import cmd

srcdir = '.'
if len (sys.argv) > 1:
    srcdir = sys.argv[1]

sys.exit (cmd.main (srcdir = srcdir))
