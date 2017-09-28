import requests

r = requests.get("http://google.com")
print(r.content, r.status_code, r.cookies, r.text, r.headers, r.encoding, sep="\n")