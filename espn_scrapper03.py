from bs4 import BeautifulSoup
import urllib2
import re

'''
This module scraps the current matches and their respective scores form espncricinfo.com
'''

while True:
	url = "http://www.espncricinfo.com/"
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)

	print soup.title.string

	para = soup.find('div',{'class':'lvScore'})
	cat = para.findAll('h3',{'class':'tbOpen'})
	for x in cat:
		print 
		print
		print
		print x.get_text()
		y = x.findNext('a',{'class':'lsBluTxt'})
		span = y.findAll('span')
		for info in span:
			print info.get_text(),
		
		

	for x in cat:
		print
		print
		print x.get_text() #get <h3> text
		div = x.findNext('div')
		tr = div.findAll('tr')
		for x in tr:
			td = x.findAll('td')
			for y in td:
				span = y.findAll('span')
				for info in span:
					print info .get_text(),
