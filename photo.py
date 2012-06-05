#coding=utf-8
import socket, time, urllib
ids = open('ids.txt').read().split('\n')[:-1]
print len(ids)
socket.setdefaulttimeout(5)
ph_url = 'http://www.npc.gov.cn/delegate/delegateList/showimg1.action?dbid=%s'

for id_ in ids:
    print id_
    tried_times = 0
    url = ph_url%id_
    while tried_times < 5:
        try:
            urllib.urlretrieve(url, 'photo2/%s.jpg'%id_)
            break
        except urllib.ContentTooShortError:
            tried_times += 1
        except socket.timeout:
            tried_times += 1
        except IOError:
            tried_times += 1
            
    time.sleep(0.1)
    
        
