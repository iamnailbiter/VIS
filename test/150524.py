__author__ = 'nailbiter'

import requests
import re

from pygoogle import pygoogle
question = raw_input("What do you want?")
g = pygoogle(question)
g.pages = 1
print '*Found %s results*' % (g.get_result_count())
urls = g.get_urls()

means_re = re.compile(r'(([A-Z]|[a-z])\w.+\.)')

def findWiki(url):
    for item in url:
        if item.find("wikipedia") != -1:
            return item


def crawl(url, maxlevel):
    if(maxlevel == 0):
        return

    req = requests.get(url)
    result = []

    if(req.status_code != 200):
        return []

    result += means_re.findall(req.text)
    return result

wiki = findWiki(urls)

if(len(wiki) > 0):
    means = crawl(wiki,10)

    for e in means:
        e = str(e)
        if e.find(question+" is") !=-1:
            print e
