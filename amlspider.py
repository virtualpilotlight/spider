# I want a spider that finds the links keeps them and saves any files it finds in along the path

"""
Initial soup # this is a html scrape of the page
Initial link scrape # takes a soup and makes a list_of_links 
# mast list of all links as a CSV

List of links
For each link in list of links
   Soup
   Scrape 

Something with cashing 

If link contains allmylove.org/audio/*.*
   Download
Else add link to list of links
"""

from bs4 import BeautifulSoup
import requests

url = "http://allmylove.org/audio/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print(soup)

counter = 0

class Soup_can:
	def __init__(self, link_name, souped):
		self.link_name = link_name
		self.souped = souped

can = Soup_can(url, false) 
print(can)
print(type(can))

urls = {
	0: {
		link_name: url, 
		souped: false
	}
}


# urls = {counter: url}

def get_links(soup):
	global counter
	global urls
	for link in soup.find_all('a'):
		new_url = url + link.get('href')
		if "?" in new_url:
			print("no soup")
		elif new_url == url:
			print("already been souped")
		elif "http://allmylove.org/audio//" in new_url:
			print("no extra slashes")
		else:
			counter += 1
			new_counter = counter 
			urls.[new_counter]{link_name: new_url, souped: False}
	return urls

get_links(soup)
print(urls)
urls.pop(0)
print(urls)
url_list = set(dict.values(urls))
print(type(url_list))

def soup_it(url_list):
	print("inside soup_it")
	for val in url_list:
		print(val)
		req = requests.get(val)
		print("req successful")
		soup = BeautifulSoup(req.text, "html.parser")
		print("soup")
		get_links(soup)
		print("links gotten")

soup_it(url_list)
print(urls)
new_dict = urls
print(type(new_dict))
# 441 total links, 15 initial
print(new_dict)

for x in new_dict.keys():
	print(x)

i = 1
while i < 15 
	


"""
if '.mp3' in val:
			# v2 did not work, this is a good place to start with the saving the files to disk
			print(f"Downloading File {name}")
			            download = req.get(href)
			            if download.status_code == 200:
			                with open(name, 'wb') as f:
			                    f.write(download.content)
			            else:
			                print(f"Download Failed For File {name}")
"""
