class decorator_class(object):
	def __init__(self,orig_func):
		self.orig_func = orig_func

	def __call__(self,*args,**kwargs):
		import time as t
		print('Initiating French Greeting Function...')
		t.sleep(2)
		return self.orig_func(*args,**kwargs)

@decorator_class
def greet_me_french(name):
	print(f"Bonjour!, {name} \n tu vas bien? ")


prmpt_usr = input("Tu t'appelles? s'il vous plaît: ")

greet_me_french(prmpt_usr)