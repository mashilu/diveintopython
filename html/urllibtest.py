import urllib

f = urllib.urlopen('http://www.baidu.com')

htmlsource = f.read(10)

f.close()

print(htmlsource)