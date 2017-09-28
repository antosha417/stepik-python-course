import re
import requests


def get_code(url):
    try:
        return requests.get(url)
    except requests.exceptions:
        return None


def get_urls(code):
    if code is not None:
        return re.findall(r'<a.*?="(.*?)"', code)
    else:
        return ''

url1, url2 = (input() for i in range(2))
sourse_code = get_code(url1)
urls1 = get_urls(sourse_code.text)
urls2 = [get_urls(get_code(url).text) for url in urls1]
for urls in urls2:
    if url2 in urls:
        print('Yes')
        break
else:
    print('No')
