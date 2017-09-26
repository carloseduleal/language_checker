import urllib
from bs4 import BeautifulSoup
import os
import sys
import re
import timeit

CRED = '\033[91m'
CEND = '\033[0m'
start = timeit.default_timer()

print " -------------------------------------------------------------------\n"
print "  db       .d8b.  d8b   db  d888b  db    db  .d8b.   d888b  d88888b   "
print "  88      d8' `8b 888o  88 88' Y8b 88    88 d8   8b 88' Y8b 88'       "
print "  88      88ooo88 88V8o 88 88      88    88 88ooo88 88      88ooooo   "
print "  88      88   88 88 V8o88 88  ooo 88    88 88   88 88  ooo 88        "
print "  88booo. 88   88 88  V888 88.  38 88b  d88 88   88 88.  38 88.       "
print "  Y88888P YP   YP VP   V8P  Y888P   Y8888P' YP   YP  Y888P  Y88888P \n"

print "       o88b  db   db d88888b  .o88b. db   dD d88888b d8888b.          "
print "     d8P  Y8 88   88 88'     d8P  Y8 88 ,8P' 88'     88  `8D          "
print "     8P      88ooo88 88ooooo 8P      88,8P   88ooooo 88oobY'          "
print "     8b      88   88 88      8b      88`8b   88      88`8b            "
print "     Y8b  d8 88   88 88.     Y8b  d8 88 `88. 88.     88 `88.          "
print "       Y88P  YP   YP Y88888P   Y88P  YP   YD Y88888P 88   YD        \n"

def getPodsAndUrls():
    filename = "urls.txt"
    urls = open(filename).read().splitlines()
    return urls

def getIgnoredWords():
    filename = "ignored_words.txt"
    ignored_words = open(filename).read().splitlines()
    return ignored_words

def extractTextFromURL(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")

    for script in soup(["script", "style"]):
        script.extract()

    textList = soup.get_text("\n").splitlines()
    return textList

def compareListsAndGetCommonValues(list1, list2):
    same_values = set(list1) & set(list2)
    same_values_without_empty_items = list(filter(None, same_values))

    return same_values_without_empty_items

def removeIgnoredWordsFromList(list):
    ignoredWordsList = getIgnoredWords()
    list_with_ignored_words_removed = [item for item in list if item not in ignoredWordsList]

    return list_with_ignored_words_removed

allPodsAndUrls = getPodsAndUrls()

for item in allPodsAndUrls:
    podAndUrls = item.split(",")
    podName = podAndUrls[0]
    url1 = podAndUrls[1]
    url2 = podAndUrls[2]

    print " -------------------------------------------------------------------"
    print "                           "+ podName
    print " -------------------------------------------------------------------\n"

    textListFromFirstUrl = extractTextFromURL(url1)
    textListFromSecondUrl = extractTextFromURL(url2)
    common_values = compareListsAndGetCommonValues(textListFromFirstUrl, textListFromSecondUrl)
    common_values_without_ignored_words = removeIgnoredWordsFromList(common_values)

    for text in common_values_without_ignored_words:
        text_with_multiple_spaces_replaced_by_single_space = re.sub('  +', '', text)
        if len(text_with_multiple_spaces_replaced_by_single_space) != 0:
            print (CRED + text_with_multiple_spaces_replaced_by_single_space + CEND)

stop = timeit.default_timer()
total_time = stop - start

mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)

sys.stdout.write("\nTotal running time: %d seconds.\n" % (secs))
