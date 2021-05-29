import numpy as np 

def function(x):

	f8 = 9
	w3 = 2
	paths = []
	try:
		if f8 > 6:
			x = x*w3
			w3 = 5*w3
			paths.append(1)
		else:
			f8 = f8-6
			paths.append(2)
		if w3 >= 7:
			x = x+f8
			f8 = f8*2
			paths.append(3)
		else:
			w3 = x-2
			x = x*f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))