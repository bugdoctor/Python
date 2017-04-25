#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'

import time
import threading

count = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    def run(self):
        global count
        time.sleep(1)
        if mutex.acquire():
            for i in range(100):
                count += 1
            print 'thread {} add 1, count is {}'.format(self.name, count)
            mutex.release()


def main():
    print "Start main threading"
    for i in range(10):
        MyThread().start()

    print "End Main threading"

if __name__ == '__main__':
    main()

