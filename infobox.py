# reference: https://www.thinbug.com/q/26476446

from bs4 import BeautifulSoup
import urllib.request as urllib2
site = "http://en.wikipedia.org/wiki/Huawei"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib2.Request(site,headers=hdr)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page.read(), features="lxml")
table = soup.find('table', class_='infobox vcard')
result = {}
exceptional_row_count = 0
for tr in table.find_all('tr'):
    if tr.find('th'):
        result[tr.find('th').text] = tr.find('td').text
    else:
        # the first row Logos fall here
        exceptional_row_count += 1
if exceptional_row_count > 1:
    print('WARNING ExceptionalRow>1: ', table)
f = open("infobox.txt", "w")
for key, value in result.items():
    print(key, ' : ', value)
    f.write(key, "\n")
    f.write(value, "\n")
f.close()