#coding=utf-8
import time
from person import parse
ids = open('ids.txt').read().split('\n')[:-1]
for id_ in ids:
    print id_
    info = parse(id_)
    for i in info:
        if i: i = i.encode('u8')
        print i
    print
    time.sleep(0.2)