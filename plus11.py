#!/usr/bin/env python                                                                                                                                                     

import sys
from time import strftime, strptime
from datetime import datetime, timedelta

#usage: ./plus11.py oldfile > newfile                                                                                                                                     

with open(sys.argv[1], 'r') as f:
    for line in f:
        orig_date = float(line[:17])
        rest = line[18:]
        yourdate = datetime.fromtimestamp(orig_date) + timedelta(hours=11)
        print str(yourdate.strftime("%Y-%m-%d_%H:%M:%S")) + ' ' + rest,
