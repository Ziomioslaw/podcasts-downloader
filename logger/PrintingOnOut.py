#!/usr/bin/python
from datetime import datetime

class PrintingOnOut():
    def message(self, msg, paramaters = None):
        if paramaters:
            paramaters = paramaters if isinstance(paramaters, list) else [paramaters]

            message = msg.replace('{}', '\033[97m{}\033[0m').format(*paramaters)
        else:
            message = msg

        date = datetime.now()
        print('[\033[2m{:%Y-%m-%d %H:%M:%S}\033[0m] {}'.format(date, message))
