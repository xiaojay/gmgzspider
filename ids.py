#coding=utf-8
import urllib, re, time
url = 'http://www.npc.gov.cn/delegate/delegateArea.action'
html = urllib.urlopen(url).read()
pattern = r'<a href="dbmd.action\?id=(.+?)">'
rs = re.findall(pattern, html)

print 'got province ids'
time.sleep(2)

for pid in rs:
    #print pid
    url = 'http://www.npc.gov.cn/delegate/dbmd.action?id=%s'%pid
    html = urllib.urlopen(url).read()
    pattern = r'<a href="viewDelegate.action\?dbid=(\d+?)" target="_blank">'
    rs = re.findall(pattern, html)
    for i in rs:
        print i
    time.sleep(2)
