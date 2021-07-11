import urllib.request, urllib.error, re

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

opener = urllib.request.build_opener()
opener.addheaders = [(b'User-Agent', b'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
opener.addheaders.append((b'Cookie', b'challenge_frame=1; spip_session=myspip_session; PHPSESSID=myPHPSESSID'))
opener.addheaders.append((b'Accept', b'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
opener.addheaders.append((b'Accept-Language', b'en-US,en;q=0.5'))
opener.addheaders.append((b'DNT', b'1'))
opener.addheaders.append((b'Connection', b'Keep-Alive'))
response = opener.open('http://challenge01.root-me.org/programmation/ch1/ch1.php?frame=1','')
html = response.read()
print(html)