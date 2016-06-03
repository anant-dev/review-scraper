import requests
import csv
from bs4 import BeautifulSoup
string = raw_input("Enter the Product Name ")
url="http://www.flipkart.com/search?q="+string
r=requests.get(url) 
soup = BeautifulSoup(r.content,"lxml")
link = soup.find_all("div",{"class":"gd-row browse-grid-row"})

for item in link :
	output= item.find("div",{"class":"swatch-container"})
	pid=output.get('data-pid')
	break
with open(string+'.csv', 'a') as csvfile:
	fieldnames = ['Author', 'date', 'Rating', 'title', 'review', 'Feedback']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in range(0,800,10):
		url="http://www.flipkart.com/"+string+"/product-reviews/ITMECC4UHBUE7VE6?pid="+pid+"&start="+str(i)
		print url
		r=requests.get(url) 
		soup = BeautifulSoup(r.content,"lxml")
		link = soup.find_all("div",{"class":"fk-review"})
		if link == []:
			print "finished"
			break
		for item in link :
			rate= item.find("div",{"class":"fk-stars"})
			review=item.find_all("span",{"class":"review-text"})[0].text.encode('utf-8')
			#print review
			feed=item.find_all("div",{"class":"review-status-bar"})[0].find_all("div",{"class":"unit"})[0].text.encode('utf-8')
			try:
				writer.writerow({ 'Author':item.find_all("div",{"class":"unit"})[0].find_all("div",{"class":"line"})[1].text,
				'date':item.find_all("div",{"class":"date"})[0].text,
				'Rating':rate.get('title'),'title':item.find_all("div",{"class":"lastUnit"})[0].find_all("div",{"class":"line"})[0].text,
				'review':review,
				'Feedback':feed})
			except Exception: 
				pass
