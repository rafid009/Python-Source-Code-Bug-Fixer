import numpy as np 

def function(x):

	o8 = x
	w5 = 9
	paths = []
	try:
		if x <= 9:
			w5 = o8-2
			paths.append(1)
		else:
			w5 = o8+o8
			o8 = w5*x
			x = x*7
			paths.append(2)
		if x <= 4:
			o8 = 9-o8
			w5 = o8-o8
			paths.append(3)
		else:
			o8 = 2/o8
			w5 = x/o8
			o8 = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w5 = x**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))