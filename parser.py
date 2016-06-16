
import urllib
import HTMLParser

url_text=[]

class parseText(HTMLParser.HTMLParser):
	def handle_data(self,data):
		if data!='\n':
			url_text.append(data)


lParser=parseText()

thisurl="http://www-rohan.sdsu.edu/~gawron/index.html"

lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
for item in url_text:
	print item