#!/usr/bin/python
import datetime

class PrintingOnOut():
    def message(self, msg):
        date = datetime.datetime.now()
        print '[%s] %s' % (date.strftime('%Y-%m-%d %H:%M:%S'), msg)
