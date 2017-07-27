#!/bin/sh
PYTHONPATH=.. python3 -m unittest discover $@ -p '*_t.py'
