#!/usr/bin/python
import datetime

class PrintingOnOut():
    def message(self, msg):
        date = datetime.datetime.now()
        print '[\033[2m%s\033[0m] %s' % (date.strftime('%Y-%m-%d %H:%M:%S'), msg)
