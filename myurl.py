from urllib.request import urlopen, Request, urlretrieve


r = urlopen(Request('http://stackoverflow.com'))
p
print(r.read())
r.close()