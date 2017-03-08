#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from webscrape import *


w = Webscraper()
w.getHtml('https://www.amazon.co.jp/product-reviews/B006D87AOM/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&showViewpoints=1&pageNumber=1')
r = w.getElementsOfType("span",contains = "review-text" ) 

#print span containing first comment of a product on amazon
print (r[0])