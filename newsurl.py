# reference: https://clay-atlas.com/us/blog/2020/01/21/python-english-note-package-googlenews-get-google-news/


# -*- coding: utf-8 -*-
from GoogleNews import GoogleNews

googlenews = GoogleNews()
googlenews.search('Huawei')
result = googlenews.result()
print(len(result))
f = open("newsurl.txt", "w")
for n in range(len(result)):
    print(n)
    for index in result[n]:
        print(index, '\n', result[n][index])
        f.write(index, "\n")
        f.write(result[n][index], "\n")
    exit()
f.close()