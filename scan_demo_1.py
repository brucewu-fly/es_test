import time
import sys

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan


def do_run(size):
    cnt = 0
    t1 = time.time()
    print "start time: %s" % t1

    es = Elasticsearch()
    for _ in scan(es, size=size):
        cnt += 1
        print cnt

    t2 = time.time()
    print "end time: %s" % t2

    diff = t2 - t1
    print "cnt: %d, cost: %ss" % (cnt, diff)
    return diff


def run(size):
    print "size: %d" % size
    n = 3
    total = 0
    a = []
    for i in range(n):
        diff = do_run(size=size)
        a.append(diff)
        total += diff

    avg = total / n
    print a
    print "avg: %ss" % avg


s = sys.argv[1]
run(int(s))
