from threading import Timer
import sys

class Progress:
    def __init__(self, type='indeterminate', msg='', success='', dotnum=3):
        self.type = type
        self.timer = None
        self.msg = msg
        self.success = success
        self.dotnum = dotnum
    def start(self):
        def recurse(i=0):
            sys.stdout.write('\r' + self.msg + ('.' * i) + ' '*(self.dotnum-i))
            sys.stdout.flush()
            self.timer = Timer(0.2, recurse, [(0 if i == self.dotnum else i+1)])
            self.timer.start()
        recurse()
    def stop(self):
        self.timer.cancel()
        sys.stdout.flush()
        sys.stdout.write('\r')
        print(self.success)
