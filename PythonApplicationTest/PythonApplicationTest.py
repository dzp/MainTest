import urllib.request
fp = urllib.request.urlopen("http://www.python.org")
for line in fp:
    print(line.strip())