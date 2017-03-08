#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from webscrape import *

w = Webscraper()

w.getHtml('https://www.reddit.com/')

r=w.getElementsOfType("a",contains = "title " ) 
iteration = 1

# print out first 3 results from reddit frontpage
for i in r[0:3]:
    i1 = i.find(" >")
    i2 = i.find("</a>")
    print("######### Thread "+ str(iteration) + "#########")
    print(i[i1+2:i2])
    iteration += 1
