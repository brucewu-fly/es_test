import time
import sys
import json
import os

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan


def do_run(f, size):
    cnt = 0
    t1 = time.time()
    print "start time: %s" % t1

    es = Elasticsearch()
    for res in scan(es, size=size):
        cnt += 1
        print cnt
        f.write(json.dumps(res) + '\n')

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
        p = os.path.join(os.getcwd(), "tmp", str(i) + ".txt")
        with open(p, "w") as f:
            diff = do_run(f, size=size)
        a.append(diff)
        total += diff

    avg = total / n
    print a
    print "avg: %ss" % avg


s = sys.argv[1]
run(int(s))
