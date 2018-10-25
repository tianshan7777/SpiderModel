#Define containers for the data


from scrapy.item import Item, Field

class HousingItem(Item):
	#HousingItem container (dictionary-like object) for scraped data
	name = Field()
	price = Field()
	#category = Field()
	#propertyType = Field()
	address = Field()
	#itemId = Field() 
	#size = Field()
	description = Field()

	