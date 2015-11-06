# -*-codeing:utf8-*-
import urllib
import re

# r = urllib.urlopen('http://hw.happyjacket.me')
# html = r.read()
# print(html)


dStr = urllib.urlopen('http://finance.yahoo.com/q/cp?s=%5EDJI+Components').read()
m = re.findall('<tr><td class=\"yfnc_tabledata1\"><b><a href=\".*?\">(.*?)</a></b></td><td class=\"yfnc_tabledata1\">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)

if m:
    print m
    print '\n'
    print len(m)
else:
    print 'not match'

