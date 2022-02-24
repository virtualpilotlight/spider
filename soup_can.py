from bs4 import BeautifulSoup
import requests

url = "http://allmylove.org/audio/"

class Soup_can:
	def __init__(self, link_name, souped):
		self.link_name = link_name
		self.souped = souped

can = Soup_can("http://allmylove.org/audio/", False) 
print(can)
print(type(can))