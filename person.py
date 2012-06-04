#coding=utf-8
import re, urllib2, socket
from BeautifulSoup import BeautifulSoup
def parse(id_):
    tried_times = 0 
    url = 'http://www.npc.gov.cn/delegate/viewDelegate.action?dbid=%s'%id_
    while tried_times < 5:
        try:
            html = urllib2.urlopen(url, timeout=3).read()
            break
        except urllib2.URLError:
            tried_times += 1
        except socket.timeout:
            tried_times += 1
            
    if tried_times >= 5:
        return ['error']
     
    b = BeautifulSoup(html)
    tb = b.find('table', attrs={'class':'table_text'})
    trs = tb.findAll('tr')

    r = []
    for tr in trs:
        data = [td.string for td in tr.findAll('td', attrs={'class':'bg2'})]
        r.extend(data)

    zw = trs[-1].find('td', attrs={'class':'bg2_1'}).string.strip()
    if not zw: zw = None
    r.append(zw)
    return r
