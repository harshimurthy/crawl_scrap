import urllib

#crawling this link
thisurl="http://www.slideshare.net/"

#open the above url
handle=urllib.urlopen(thisurl)

#read the url
html_gunk=handle.read()

#print first 150 lines of html page
print html_gunk[:150]

#prints entire page in html
print html_gunk