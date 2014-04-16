from bs4 import BeautifulSoup
import urllib2

url = "http://www.google.com"
content  = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
print soup.get_text()

soup = BeautifulSoup("<html>data</html>")

sibling_soup = BeautifulSoup('<a><b>text1</b><c>text2</c></a>\
<a href="sdfdssdasda">linktop</a><a href="dsasdadad">link bottom</a>');
print(sibling_soup.prettify())

print sibling_soup.b.next_sibling
print sibling_soup.c.previous_sibling

print sibling_soup.b.next_sibling.get_text()
print sibling_soup.c.previous_sibling.get_text()

print sibling_soup.b.previous_sibling
print sibling_soup.c.next_sibling

link = soup.a
print "link"
print link
link.next_sibling
link.next_sibling
