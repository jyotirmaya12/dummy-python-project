#!/usr/bin/env python
import sys, re

lines = sys.stdin.readlines()
for l in lines:
    m = re.match("\s*password (.*)", l)
    if m:
        print l[0:10], m.groups(1)[0][0:8], "...REDACTED...", m.groups(1)[0][-4:]
    else:
        print l
