# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 03:01:02 2019

@author: Dictador
"""
from __future__ import division
import re, os, sys, errno, glob
import json
import requests
from bs4 import BeautifulSoup
from time import sleep
import datetime as dt
#import HTML

# Login to your ali account first. Make sure webpage is in english, dollars (or any other language, currency, but keep the things consistent each time you save the json)
# The link below placed in your webbrowser will download your ali cart in json format.
# Save it from your webbrowser to a local file under a name ali_cart_2020_12_04.json
#
# https://shoppingcart.aliexpress.com/api/1.0/cart/items.do?currentPage=0&uniqueId=1

file_names = []
for name in glob.glob('ali_cart_*.json'): # saved files are named 'ali_cart_2020_11_28.json'
    print(name)
    file_names.append(name)

file_names = sorted(file_names)
files_n =len(file_names)

with open(file_names[-1], encoding="utf8") as json_file:
    data = json.load(json_file)


#products_list = [{
#                 'productId':'',
#                 'productKey':'',
#                 'itemId':'',
#                 'detailUrl':'',
#                 'title':'',
#                 'price':'',
#                 'currencyCode':'',
#                 'priceMin':'',
#                 'priceMax':'',
#                 'priceAvg':'',
#                 'coupons':''
#                 }]
products_list = []
for store in data['stores']:
    #print(store)
    for item in store["storeList"]:
        for product in item["products"]:
            products_list.append( {  
                                'productId':product['productId'],
                                'productKey':product['productKey'],
                                'itemId':product['itemId'],
                                'detailUrl':product['detailUrl'],
                                'title':product['title'],
                                'price':product['cost']['price']['amount'],
                                'currencyCode':product['cost']['price']['currencyCode'],
                                'priceMin':product['cost']['price']['amount'],
                                'priceMax':product['cost']['price']['amount'],
                                'priceAvg':product['cost']['price']['amount']
                            } )
#products_list['coupons'].append(
#print(n,'   ',product['title'][0:40],'        ',str(product['cost']['price']['amount']),'  ',product['cost']['price']['currencyCode'])

for n in range(0,files_n-1):
    with open(file_names[-n], encoding="utf8") as json_file:
        data = json.load(json_file)
    for i,x in enumerate(products_list):
        for store in data['stores']:
            for item in store["storeList"]:
                for product in item["products"]:
                    if x['productId'] == product['productId']:
                        products_list[i]['priceMin'] = min(product['cost']['price']['amount'], products_list[i]['priceMin'])
                        products_list[i]['priceMax'] = max(product['cost']['price']['amount'], products_list[i]['priceMax'])
                        products_list[i]['priceAvg'] = ((products_list[i]['priceAvg']*100) + (product['cost']['price']['amount']*100))/200

# This section prints the analysis results on the screen.
# Products priced higher than the lowest price ever recorded are printed in black
# Products priced at the lowest price ever recorded are printed in red
# Products priced lower than the lowest price ever recorded are printed in purple

for n,product in enumerate(products_list):
    if product['price'] == product['priceMin']:
        print(n+1, '\t\33[31;91m', product['title'][0:30], '\t', product['price'], ' ' ,product['currencyCode'], '\t' ,product['priceAvg'], '\t' ,product['priceMin'],'\33[0m')
    elif (product['price'] < product['priceMin']):
        print(n+1, '\t\33[35;91m', product['title'][0:30], '\t', product['price'], ' ' ,product['currencyCode'], '\t' ,product['priceAvg'], '\t' ,product['priceMin'],'\33[0m')
    else:
        print(n+1, '\t', product['title'][0:30], '\t', product['price'], ' ' ,product['currencyCode'], '\t' ,product['priceAvg'], '\t' ,product['priceMin'])
