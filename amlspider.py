from bs4 import BeautifulSoup
import requests

url = "http://allmylove.org/audio/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

print(soup)

# fix this classS


counter = 0

urls = {
	0: {
		link_name: url, 
		souped: False
	}
}

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
			urls.update({new_counter: {link_name: new_url, souped: False}})

get_links(soup)
print(urls)

urls.update({0: {link_name: url, souped: True}})

for x in urls:
	print(urls[x])
	print(type(x))

url_list = set(dict.values(urls))
print(url_list)
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

