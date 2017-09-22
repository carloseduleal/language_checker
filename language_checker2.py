import urllib
from bs4 import BeautifulSoup
import sys
import re
import timeit

start = timeit.default_timer()

print " -------------------------------------------------------------------\n"
print "  db       .d8b.  d8b   db  d888b  db    db  .d8b.   d888b  d88888b "
print "  88      d8' `8b 888o  88 88' Y8b 88    88 d8   8b 88' Y8b 88'     "
print "  88      88ooo88 88V8o 88 88      88    88 88ooo88 88      88ooooo "
print "  88      88   88 88 V8o88 88  ooo 88    88 88   88 88  ooo 88      "
print "  88booo. 88   88 88  V888 88.  38 88b  d88 88   88 88.  38 88.     "
print "  Y88888P YP   YP VP   V8P  Y888P   Y8888P' YP   YP  Y888P  Y88888P \n"

print "       o88b  db   db d88888b  .o88b. db   dD d88888b d8888b. "
print "     d8P  Y8 88   88 88'     d8P  Y8 88 ,8P' 88'     88  `8D "
print "     8P      88ooo88 88ooooo 8P      88,8P   88ooooo 88oobY' "
print "     8b      88   88 88      8b      88`8b   88      88`8b   "
print "     Y8b  d8 88   88 88.     Y8b  d8 88 `88. 88.     88 `88. "
print "       Y88P  YP   YP Y88888P   Y88P  YP   YD Y88888P 88   YD \n"
print " -------------------------------------------------------------------\n"

firstUrl = sys.argv[1]
secondUrl = sys.argv[2]

def extractTextFromTheURL(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    for script in soup(["script", "style"]):
        script.extract()

    textList = soup.get_text("\n").splitlines()
    return textList

textListFromFirstUrl = extractTextFromTheURL(firstUrl)
textListFromSecondUrl = extractTextFromTheURL(secondUrl)

same_values = set(textListFromFirstUrl) & set(textListFromSecondUrl)
result = list(filter(None, same_values))

CRED = '\033[91m'
CEND = '\033[0m'

for text in result:
    textWithMultipleSpacesReplaceSingleSpace = re.sub(' +', '', text)
    if len(textWithMultipleSpacesReplaceSingleSpace) != 0:
        print (CRED + textWithMultipleSpacesReplaceSingleSpace.lstrip() + CEND)

stop = timeit.default_timer()
total_time = stop - start

mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)

sys.stdout.write("\nTotal running time: %d seconds.\n" % (secs))
