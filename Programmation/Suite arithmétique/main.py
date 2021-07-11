import urllib2, re

def arith_func(n, sign, alpha, beta, u0):
    result = u0
    if n == 0:
        return u0
    if sign == '-':
        for i in range(1,n+2):
            result = alpha + result - (i-1)*beta
    else:
        for i in range(1,n+2):
            result = alpha + result + (i-1)*beta
    return result

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
opener.addheaders.append(('Cookie', 'challenge_frame=1; spip_session=myspip_session; PHPSESSID=myPHPSESSID'))
opener.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
opener.addheaders.append(('Accept-Language', 'en-US,en;q=0.5'))
opener.addheaders.append(('DNT', '1'))
opener.addheaders.append(('Connection', 'Keep-Alive'))
response = opener.open('http://challenge01.root-me.org/programmation/ch1/ch1.php?frame=1','')
html = response.read()
print(html)
match = re.search(r'U<sub>n\+1</sub> = \[ (.*) \+ U<sub>n</sub> ] (.) \[ n \* (.*) ]<br />\nU<sub>0</sub> = (.*)\n<br />', html)
alpha = int(match.group(1))
sign = match.group(2)
beta = int(match.group(3))
u0 = int(match.group(4))
match = re.search(r'Trouver le terme n&deg;(.*) de cette suite.', html)
n = int(match.group(1))
result = arith_func(n, sign, alpha, beta, u0)
print(result)
submit_url = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php?resultat='+str(result)
response = opener.open(submit_url,'')

file_handle = open('result.html', 'w')
while 1:
    data = response.read()
    if not data:
        break
    file_handle.write(data)
file_handle.close