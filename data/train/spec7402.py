import numpy as np 

def function(x):

	w8 = 0
	y6 = x
	paths = []
	try:
		if x <= 0:
			x = 5*5
			w8 = y6-9
			w8 = y6/x
			paths.append(1)
		else:
			w8 = w8/y6
			paths.append(2)
		if x < 8:
			w8 = y6*w8
			y6 = y6-9
			y6 = 6/y6
			paths.append(3)
		else:
			x = 3-y6
			w8 = w8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w8 = x**0.5
		return w8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))