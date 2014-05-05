from bs4 import BeautifulSoup
import urllib2
import re
url = "http://www.espncricinfo.com/ci/engine/match/scores/live.html"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)

print soup.title.string


head = soup.findAll('p',{'class':'LivScrHdTxt'})
'''
for x in head:
	print x.find('b').get_text()
'''
#head is a list 
## access it by using loop 
##
print head[0].find('b').get_text()



#division = soup.findAll('div',attrs={'style' : 'margin:0 0 8px 10px;'})
#print division[0].findAll('p')
para = soup.find('p',{'class':'potMatchHeading'})
print para
for x in para:
	print para.get_text()
