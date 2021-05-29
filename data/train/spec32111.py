import numpy as np 

def function(x):

	w8 = x
	f7 = 6
	x = 0
	paths = []
	try:
		if w8 >= 0:
			w8 = 1*w8
			paths.append(1)
		else:
			x = x*7
			f7 = x/3
			paths.append(2)
		if w8 >= 9:
			x = x-w8
			paths.append(3)
		else:
			x = 6-f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))