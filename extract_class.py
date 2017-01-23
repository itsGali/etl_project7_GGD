#!/bin/env python2.7
# -*- coding: utf-8 -*-
import csv
import json
from bs4 import BeautifulSoup
import urllib, sys
from unidecode import unidecode

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding="utf-8"))

product_info = {}
product_opinion = {}
product_cons_pros = {}

if sys.argv[1] == 0:
    print("Nie wprowadzono parametru ID Produktu.")
    raise SystemExit
else:
    r = urllib.urlopen('https://www.ceneo.pl/' + str(sys.argv[1])).read()
    soup = BeautifulSoup(r.decode('utf-8','ignore'), "html.parser")

    if not soup.select('div.product-content'):
        print("No Product Content")
    else:
        product_category = ""
        user_product_review = ""

        for category in soup.findAll('span', {'itemprop': 'title'}):
            product_category = "".join(category.text)
        product_title = soup.find('h1', {'class': 'product-name'})
        product_producer = []
        if not soup.select('div.product-full-description'):
            print("No Product Description Content")
        else:
            """miejsce na wyciagniecie calej tabeli specyfikacji produktu
            divs = soup.findAll("table")
            for div in divs:
                row = ''
                rows = div.findAll('tr')
                for row in rows:
                    if (row.text.find("Producent") > -1):
                        product_producer.append(str(row.text).replace("\r","").replace("\n",""))
                        #if product_producer.replace("\n"," ").split()[1] != "":
                           # print("Ok,produkt posiada nazwe producenta.")
            """
        product_extra_info = soup.find('div', {'class': 'ProductSublineTags'})
        
	if soup.find('span', {'class': 'product-score'}):
		product_overal_rating = soup.find('span', {'class': 'product-score'})['content']
	else:
		produc_veral_rating = "None"
        product_review_count = soup.find('span', {'itemprop': 'reviewCount'})
        
	if soup.find('meta', {'property': 'og:brand'}):
		producer = soup.find('meta', {'property': 'og:brand'})['content']
        else:
		producer = "None"
	model = soup.find('strong', {'class': 'js_searchInGoogleTooltip'})

        #print("product_producer: " + str(u''.join(producer).encode('utf-8').strip().replace("  ", " ")))
        #print("product_model:" + str(u''.join(model.text).encode('utf-8').strip().replace("  ", " ")))
        #print("product_category: " + str(u''.join(product_category).encode('utf-8').strip().replace("  ", " ")))
        #print("product_extra_info: " + str(u''.join(product_extra_info.text).encode('utf-8').strip().replace("  ", " ")))
        #print("product_overal_rating: " + str(u''.join(product_overal_rating).encode('utf-8').strip().replace("  ", " ")))
        #print("product_review_count: " + str(u''.join(product_review_count.text).encode('utf-8').strip().replace("  ", " ")))

        product_info = {
            'product_id': str(sys.argv[1]), 'producer': remove_non_ascii(str(u''.join(producer).encode('utf-8').strip().replace("  ", " "))), 'model': remove_non_ascii(str(u''.join(model.text).encode('utf-8').strip().replace("  ", " "))), 'category': remove_non_ascii(str(u''.join(product_category).encode('utf-8').strip().replace("  ", " "))),
                               'extra_info': remove_non_ascii(str(u''.join(product_extra_info.text).encode('utf-8').strip().replace("  ", " "))), 'review': remove_non_ascii(str(u''.join(product_overal_rating).encode('utf-8').strip().replace("  ", " "))),
                               'reviews_count': remove_non_ascii(str(u''.join(product_review_count.text).encode('utf-8').strip().replace("  ", " ")))}

        reviews_per_page = 10
        pages_to_iterate = 0

        product_reviewers = []
        product_reviewers_score = []
        product_review_time = []
        product_review_body = []
        product_review_summary = []

        product_review_id = []
        product_review_cons = []
        product_review_pros = []

        product_review_helpful = []
        product_review_unhelpful = []

        if (int(product_review_count.text) % reviews_per_page == 0):
            pages_to_iterate = (int(product_review_count.text) / reviews_per_page)
            #print("review_pages: " + str(pages_to_iterate))
        else:
            pages_to_iterate = (int(product_review_count.text) / reviews_per_page) + 1
            #print("review_pages: " + str(pages_to_iterate))
            i = 1
            while i <= pages_to_iterate:
                #print(i)
                url_rev = urllib.urlopen('https://www.ceneo.pl/' + str(sys.argv[1]) + '/opinie-' + (str(i))).read()
                soup_reviews = BeautifulSoup(url_rev, "html.parser")

                for pr in soup_reviews.find_all('div', {'class': 'product-reviewer'}):
                    product_reviewers.append(remove_non_ascii(str(u''.join(pr.text).encode('utf-8').strip().replace("  ", " "))))

                for rsc in soup_reviews.find_all('span', {'class': 'review-score-count'}):
                    product_reviewers_score.append(remove_non_ascii(str(u''.join(rsc.text).encode('utf-8').strip().replace("  ", " "))))

                for review_time in soup_reviews.findAll('time'):
                    if review_time.has_attr('datetime'):
                        product_review_time.append(review_time['datetime'])

                for prb in soup_reviews.find_all('p', {'class': 'product-review-body'}):
                    product_review_body.append(remove_non_ascii(str(u''.join(prb.text).encode('utf-8').strip().replace("  ", " "))))

                for prs in soup_reviews.find_all('div', {'class': 'product-review-summary'}):
                    product_review_summary.append(remove_non_ascii(str(u''.join(prs.text).encode('utf-8').strip().replace("  ", " "))))
                # wyciagam id opoini i na jej podstawie wyciagne ilosc lapek w gore dla danej opini i ilosclapek w dol
                for prid in soup_reviews.find_all('a', {
                    'class': 'capitalize hover-highlight review-link abuse-ico js_report-product-review-abuse'}):
                    if prid.has_attr('data-review-id'):
                        product_review_id.append(prid['data-review-id'])
                        for helpful in soup_reviews.find_all('span', {
                            'id': ('votes-yes-' + (prid['data-review-id']))}):
                            product_review_helpful.append(remove_non_ascii(str(u''.join(helpful.text).encode('utf-8').strip().replace("  ", " "))))
                        for unhelpful in soup_reviews.find_all('span', {
                            'id': ('votes-no-' + (prid['data-review-id']))}):
                            product_review_unhelpful.append(remove_non_ascii(str(u''.join(unhelpful.text).encode('utf-8').strip().replace("  ", " "))))

                for a in soup_reviews.find_all('div', {'class': 'show-review-content content-wide'}):
                    for xd in a.find_all('button', {'class': 'vote-yes js_product-review-vote js_vote-yes'}):
                        #print(xd['data-review-id'])
                        for b in a.find_all('div', {'class': 'content-wide-col'}):
                            for c in b.find_all('div',{'class': 'product-review-pros-cons'}):
                                children = c.find_all('div',{'class': 'pros-cell'})
                                for child in children:
                            	#print(child.text)
					chi = c.find_all('div', {'class': 'cons-cell'})
	                                for chil in chi:
                                    #print(chil.text)
                                		product_cons_pros.setdefault(xd['data-review-id'], {'zalety': remove_non_ascii(str(u''.join(child.text).encode('utf-8').strip().replace("  ", " "))), 'wady': remove_non_ascii(str(u''.join(chil.text).encode('utf-8').strip().replace("  ", " ")))})

        	i += 1

        product_opinion = dict((z[0], list(z[1:])) for z in
                               zip(product_review_id, product_reviewers, product_reviewers_score, product_review_summary,
                                   product_review_time, product_review_body, product_review_helpful,
                                   product_review_unhelpful))
        product_opinion = {str(sys.argv[1]): product_opinion}
        pages_to_iterate = 0

        #print(product_info)
        #print(product_opinion)
        #print(product_review_id)
        #print(product_cons_pros)

        with open('product_info.json', 'w+') as pi:
            json.dump(product_info, pi)
        with open('product_opinion.json', 'w+') as po:
            json.dump(product_opinion, po)
        with open ('product_opinion_pros_cons.json', 'w+') as popc:
            json.dump(product_cons_pros, popc)

	print("Wykonano")
	sys.exit(0)
