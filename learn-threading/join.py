#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'ghost'


import time
import threading


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print 'thread {}, @number: {}'.format(self.name, i)
            time.sleep(1)

def main():
    print "Start main threading"

    threads = [MyThread() for i in range(3)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print "End Main threading"


if __name__ == '__main__':
    main()