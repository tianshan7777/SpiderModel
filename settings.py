BOT_NAME = 'RIGHTMOVE'
SPIDER_MODULE = ['Spider_2.spiders']
ITEM_PIPELINES = ['Spider_2.pipelines.RightMovePipeline']

DATABASE = {
	'drivername' : 'postgres',
	'host' : 'localhost',
	'port': '5432',
	'username' : 'tianshan',
	'password' : '',
	'database' : 'scrape'
}

