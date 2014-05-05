from bs4 import BeautifulSoup
import urllib2
import re
url = "http://www.imdb.com/movies-in-theaters/?ref_=hm_otw_sm"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
#data =  soup.prettify()
#print data
#print soup.get_text()
'''
for each_div in soup.findAll('div',{'class': 'list detail sub-list'}):
	print each_div
'''	
	
print
print 
print

InputTag=  soup.findAll(attrs={"itemprop" : "url"})

#output = [s[0]["title"] for s in InputTag]
#print output

#for x in InputTag:
#	print x["title"]
#no of movies and their characters
'''
for x in InputTag:
	print x.get_text()
'''	
# only movies
InputTag=  soup.findAll('h4',attrs={"itemprop" : "name"})
for x in InputTag:
	lis = x	.find('a',attrs={"itemprop" : "url"}).get_text()
	print lis

print 
print
print

# movies categorry wise
InputTag =  soup.findAll('div',{'class': 'list detail sub-list'})
for x in InputTag:
	lis = x.find('h3').get_text()
	print lis
	print
	InputMovie =  x.findAll('h4',attrs={"itemprop" : "name"})
	for x in InputMovie:
		lis = x	.find('a',attrs={"itemprop" : "url"}).get_text()
		print lis
	print
	print

