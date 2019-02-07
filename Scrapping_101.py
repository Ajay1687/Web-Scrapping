import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from bs4 import NavigableString as ns

my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+cards&N=-1&isNodeId=1"

uClient = ureq(my_url)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html,"html.parser")

grids = page_soup.findAll("div",{"class":"items-view is-grid"})
grid_total = []
for grid in grids:
	grid_total += grid  #Has all the containers in that grid

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






