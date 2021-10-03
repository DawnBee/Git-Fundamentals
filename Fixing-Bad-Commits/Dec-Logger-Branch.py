def logger(orig_func):
	import logging

	def wrapper_function(*args,**kwargs):
		logger = logging.getLogger(__name__)
		logger.setLevel(logging.INFO)

		file_handler = logging.FileHandler('{}.txt'.format(orig_func.__name__))
		logger.addHandler(file_handler)

		formatter = logging.Formatter('[%(asctime)s] (%(levelname)s): %(message)s')
		file_handler.setFormatter(formatter)
		
		logger.info('Update: Logged an Entry')

		return orig_func(*args,**kwargs)
	return wrapper_function

@logger
def journal(entry_num):
	from datetime import date as dt
	print(f"Entry# {entry_num}: {'{:%B %d, %Y}'.format(dt.today())}")

journal(1)
		