from bs4 import BeautifulSoup
import urllib2
import re
url = "http://www.imdb.com/movies-in-theaters/?ref_=hm_otw_sm"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)

'''
IMDB Scrapper 01 using BeautifulSoup 4
This module extracts the upcomming movies and the movies currently on theater

'''

# only movies without category
InputTag=  soup.findAll('h4',attrs={"itemprop" : "name"})
for x in InputTag:
	lis = x	.find('a',attrs={"itemprop" : "url"}).get_text()
	print lis

print 
print
print

# movies category wise
InputTag =  soup.findAll('div',{'class': 'list detail sub-list'})
for x in InputTag:
	lis = x.find('h3').get_text()
	print lis
	print
	InputMovie =  x.findAll('h4',attrs={"itemprop" : "name"})
	for x in InputMovie:
		lis = x	.find('a',attrs={"itemprop" : "url"}).get_text()
		print lis
