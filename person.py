#coding=utf-8
import re, urllib
from BeautifulSoup import BeautifulSoup
def parse(id_):
    url = 'http://www.npc.gov.cn/delegate/viewDelegate.action?dbid=%s'%id_
    html = urllib.urlopen(url).read()

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
