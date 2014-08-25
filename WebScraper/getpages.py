from urllib import urlopen
from lxml.html import fromstring

def getpages(url):
    down=urlopen(url).read()
    obj=fromstring(down)
    obj.make_links_absolute(url)
    return obj
