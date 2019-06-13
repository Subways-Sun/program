#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json
import os

appKey = '170b4605cce9355d'
secretKey = 'zwsQ0tDY722I5dbiSsmIdzf1RmM3QAU8'

 
httpClient = None
fromLang = 'EN'
toLang = 'zh-CHS'
salt = random.randint(1, 65536)


if os.path.exists('3.xml'):
    os.remove('3.xml')
f = open('3.xml', 'a')
f.write("<wordbook>")
for word in open('1.txt'):
    q = word.strip()
    if q == "":
        continue
    sign = appKey+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = '/api'
    myurl = myurl+'?appKey='+appKey+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    try:
        httpClient = httplib.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
     
        #response是HTTPResponse对象
        response = httpClient.getresponse().read()
        #print response
        result = json.loads(response)
        if 'basic' in result:
            f.write("<item> <word>" + q + "</word><trans><![CDATA[" + ' / '.join(result['basic']['explains']).encode('utf-8') + "]]></trans><phonetic><![CDATA[]]></phonetic><tags></tags><progress>1</progress></item>\n")
        elif 'translation' in result:
            f.write("<item> <word>" + q + "</word><trans><![CDATA[" + ' / '.join(result['translation']).encode('utf-8') + "]]></trans><phonetic><![CDATA[]]></phonetic><tags></tags><progress>1</progress></item>\n")
        else :
            raw_input(q + "\terror")
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
f.write("</wordbook>")
f.close()
