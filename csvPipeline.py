import csv

class csvWriter():

	def write_csv(item_attr):

		with open('houses_file.csv', mode='w') as houses_file:
			houses_writer = csv.writer(houses_file, delimiter=',', quatechar='"', quating=csv.QUOTE_MINIMAL)

			houses_writer.WRITEROW(item_attr)