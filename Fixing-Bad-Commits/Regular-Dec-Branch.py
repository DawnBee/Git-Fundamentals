def html_tag(tag):
	def wrap_text(msg):
		print('<{1}> {0} </{1}>'.format(msg,tag))
	return wrap_text


disp_p = html_tag('p')	
disp_p('This is our first paragraph')

def decorator_function(orig_func):
	def wrapper_function(*args,**kwargs):
		print("Function Initiated: '{}'".format(orig_func.__name__))
		return orig_func(*args,**kwargs)
	return wrapper_function


@decorator_function
def greet_me(ask_usr):
	print(f"Hello {ask_usr}, how are you?")

ask_usr = input('Please enter your name: ')
greet_me(ask_usr)