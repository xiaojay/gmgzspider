#coding=utf-8
import time, logging
from person import parse
logfile = 'fetch.log'
logging.basicConfig(level=logging.INFO, format='%(levelname)s - - %(asctime)s %(message)s', 
                    datefmt='[%d/%b/%Y %H:%M:%S]', filename=logfile)

ids = open('ids.txt').read().split('\n')[:-1]
fetched = 0
for id_ in ids:
    print id_
    info = parse(id_)
    for i in info:
        if i: i = i.encode('u8')
        print i
    print
    
    fetched += 1
    if fetched%100 == 0:
        logging.info('fetched %i.'%fetched)
        logging.info('fetched id_ %s just now.'%id_)
    time.sleep(0.2)
    