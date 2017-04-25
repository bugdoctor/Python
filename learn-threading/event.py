#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, event):
        super(MyThread, self).__init__()
        self.event = event


    def run(self):
        print "thread {} is ready ".format(self.name)
        self.event.wait()
        print "thread {} run".format(self.name)


signal = threading.Event()


def main():
    start = time.time()
    for i in range(3):
        t = MyThread(signal)
        t.start()
    time.sleep(3)
    print "after {}s".format(time.time() - start)
    signal.set()


if __name__ == '__main__':
    main()