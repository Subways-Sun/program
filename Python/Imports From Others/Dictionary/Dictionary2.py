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
if os.path.exists('Output.txt'):
    os.remove('Output.txt')
f = open('Output.txt', 'a')
for word in open('Input.txt'):
    q = word.strip()
    if q == '':
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
     
        response = httpClient.getresponse().read()
        result = json.loads(response)
        if 'basic' in result:
            if result['basic']['explains'][-1].startswith('n. ('):
                f.write(q + '\t' + ' / '.join(result['basic']['explains'][0:-1]).encode('utf8') + '\n')
            else :
                f.write(q + '\t' + ' / '.join(result['basic']['explains']).encode('utf8') + '\n')
        elif 'translation' in result:
            if result['translation'][-1].startswith('n. ('):
                f.write(q + '\t' + ' / '.join(result['translation'][0:-1]).encode('utf8') + '\n')
            else :
                f.write(q + '\t' + ' / '.join(result['translation']).encode('utf8') + '\n')
        else :
            raw_input(q + '\terror')
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
f.close()
