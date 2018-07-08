import time
import sys
from multiprocessing import Pool

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan


def slice_scan(size, slice_id, slice_max):
    es = Elasticsearch()
    cnt = 0
    for _ in scan(es, query={"slice": {"id": slice_id, "max": slice_max}}, size=size):
        cnt += 1
        print cnt
    print "sliced_id=%d, cnt=%d" % (slice_id, cnt)


def do_run(size, slice_max):
    t1 = time.time()
    print "start time: %s" % t1

    p = Pool()
    for i in range(slice_max):
        p.apply_async(slice_scan, args=(size, i, slice_max))

    p.close()
    p.join()

    t2 = time.time()
    print "end time: %s" % t2

    diff = t2 - t1
    print "cost: %ss" % diff
    return diff


def run(size, slice_max):
    print "size: %d" % size
    n = 3
    total = 0
    a = []
    for i in range(n):
        diff = do_run(size=size, slice_max=slice_max)
        a.append(diff)
        total += diff

    avg = total / n
    print a
    print "avg: %ss" % avg


arg1 = sys.argv[1]
arg2 = sys.argv[2]
run(int(arg1), int(arg2))
