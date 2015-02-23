#!/usr/bin/env python

import sys
import datetime
import dateutil.parser

#usage: ./plus11.py oldfile > newfile

#2014-01-21T00:09:21+0000
#date_object = datetime.strptime(orig, '%Y-%m-%d %H:%M:%S')
with open(sys.argv[1], 'r') as f:
    for line in f:
        orig_date = line[1:20]
        rest = line[21:]
        date_object = datetime.datetime.strptime(orig_date, '%Y-%m-%d %H:%M:%S')
        print str(date_object + datetime.timedelta(hours=11))+rest,
