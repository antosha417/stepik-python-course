import re
import requests


def get_code(url):
    try:
        return requests.get(url)
    except requests.exceptions:
        return None


def get_urls(code):
    if code is not None:
        return re.findall(r'<a.*?href[="\' ]*(.*?)["\']', code, re.IGNORECASE)
    else:
        return ''

start_url = input()
urls = get_urls(get_code(start_url).text)

#test = '''
#    <a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">Хостинг</a></li>
#    <a href="http://www.m-2.ru/">M2</a>
#    <a target="_top" href="http://banner.rbc.ru/banredir.cgi?lid=firstpage_left" empty="true" style="display:none"></a>
#<a href="http://biztorg.ru:80/main_services_new.shtml">Оценка бизнеса</a>
#<a href="http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbcdaily.ru/mainnews.rss" class="flRight small" style="margin:0 0 0 5px;">
#<a href="test#test">

#urls = get_urls(test)

res = set()
for url in urls:
    site = re.findall(r'(.*?(//|\.)*?)?(.*?\.[^/:]*)', url, re.IGNORECASE)
    try:
        if len(site[0][2]) > 2:
            res.add(site[0][2])
    except IndexError:
        pass
answ = list(res)
answ.sort()
print(answ)
