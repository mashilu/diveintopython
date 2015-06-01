import urllib

sock = urllib.urlopen("http://www.baidu.com")
htmlsource = sock.read()
sock.close()

print(htmlsource)