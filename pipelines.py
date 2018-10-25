from sqlalchemy.orm import sessionmaker
from models import Items, db_connection, create_items_table

class RightMovePipeline(object):
	#RightMove pipeline for stroig scraped items in the database
	def _init_(self):
		#Initialise database connection and sessionmaker
		#Create items table

		engine = db_connection()
		create_items_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item, spider)
		#Save items in the database
		#This method is called for every item pipeline component
		session = self.Session()
		item = Items(**item)

		try:
			session.add(item)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()

		return item
