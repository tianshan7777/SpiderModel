from scrapy.spider import BaseSpider
from spider_v1.items import HousingItem
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
from scrapy.selector import Selector

class HousingSpider(BaseSpider):
	#Spider for regularly update www.rightmove.co.uk/overseas-property-for-sale/Budapest.html
	name = "rightmove"
	allowed_domains = ["rightmove.co.uk"]
	start_urls = ["https://www.rightmove.co.uk/overseas-property-for-sale/Budapest.html"]

	items_list_xpath = '//div[@class="l-searchResults"]/div[@class="l-searchResult is-list"]'

	#A dictionary of all of our items we defined in Items.py earlier with the associated values as their XPaths, relative to items_list_xpath
	item_fields = {
		'name' : './/h2[@class="propertyCard-title"/text()]',
		'price' : './/div[@class="propertyCard-priceValue"]/text()',,
		'address' : './/address/span/text()',
		'description' : './/span[@itemprop="description"]/text()
	}

	#The response parameter is what the spider gets vack in return after making a request to the hungarianhouses website
	#We are parsing that response with our XPaths
	def parse(self, response):
		#Initiate HtmlXpathSelector()n by giving it the parameter, response
		selector = HtmlXpathSelector(response)

		#Iterate over houses
		for house in selector.select(self.items_list_xpath):
			loader = XPathItemLoader(HousingItem(), selector = house)

			#Define processors
			#We wet up the process for house data first by tripping our white-space of unicode strings then join the data together
			#MapCompose() will help the input processing of our data and will be used to help clean up the data that we extract
			#Join() will help the output processing of our data, and will join together the elements that we process.
			loader.default_input_processor = MapCompose(unicode.strip)
			loader.default_output_processor = Join()

			#Iterate over fields and add xpaths to the loader
			#iteritems() returns an iterator object which allows you to iterate the (key, value) of items in a dictionary  
			for field, xpath in self.item_fields.iteritems():
				loader.add_xpath(field, xpath)
			#load_item() whill grab each item field for each deal, get its xpath, process its data with the input & output processer
			yield loader.load_item()
