import re
import sys

for line in sys.stdin:
    val = line.strip()
    (year, temp) = (val[15:19], val[40:45])
    print("%s\t%s" % (year, temp))
