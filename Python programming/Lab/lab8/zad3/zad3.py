#!/usr/bin/env python3
import urllib.request
import urllib.parse

url ="https://www.netflix.com"
try:
    response = urllib.request.urlopen(url)
    print("Zawartosc url: ", response.read())
    urlParse = urllib.parse.urlparse(url)
    print("\n\nWyjscie  strony po sparsowaniu", urlParse)
    print("\n\n Zwrocony Naglowek strony  ",response.info())
    print("\nAdres url z odpowiedzi strony ", response.geturl())
except urllib.error.HTTPError as e:
    print("Problemy z adresem url {} {}".format(e.code, e.reason))


