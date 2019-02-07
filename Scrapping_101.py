#Importing the libraries
import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from bs4 import NavigableString as ns

#URL from which I would scrap the data.
my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+cards&N=-1&isNodeId=1"

#Initializing the url object to do the request
uClient = ureq(my_url)

#Reading the response html page onto another object
page_html = uClient.read()

#Closing the connection
uClient.close()


#Making use of the Soup library, to parse the html page
page_soup = soup(page_html,"html.parser")

#The site had products aligned into grids, retireving all the grids here(in total there were 3 in this URL)
grids = page_soup.findAll("div",{"class":"items-view is-grid"})
grid_total = []

#Combining all the grids into single one
for grid in grids:
	grid_total += grid  #Has all the containers in that grid


#Initializing the csv file, into which we will write the products details

fileName = "ProductList.csv"
f = open(fileName,"w")

headers = "brand_name,product_name,shipping_cost\n"

f.write(headers)


i = 1
for i in range(len(grid_total)):
	#First and last elemnt of grid_total arenew line chars
	if isinstance(grid_total[i],ns):
		continue
	else:
		container = grid_total[i].findAll("div",{"class":"item-branding"})
		#Also these are list hence using [0]
		#Brand name
		brand = container[0].a.img["title"]

		#Product Name
		product_name = grid_total[i].findAll("a",{"class":"item-title"})[0].text

		#Shipping cost
		ship_cost = grid_total[i].findAll("li",{"class":"price-ship"})[0].text.strip()


		#print("Brand Name:",brand)
		#print("Product name:",product_name)
		#print("Shipping Cost:",ship_cost)

		f.write(brand + "," + product_name.replace(",","|") + "," + ship_cost + "\n")
f.close()






