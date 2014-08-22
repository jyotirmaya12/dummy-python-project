#!/usr/bin/env python
import sys, time

for x in range(20):
    print "output line ", x
    sys.stdout.flush()
    time.sleep(2)
