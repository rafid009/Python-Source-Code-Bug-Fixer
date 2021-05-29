import numpy as np 

def function(x):

	y0 = x
	w8 = x
	x = 4
	paths = []
	try:
		if w8 >= 5:
			w8 = w8/1
			x = x-6
			paths.append(1)
		else:
			w8 = 6*w8
			paths.append(2)
		if y0 < 6:
			x = w8*x
			x = x+7
			paths.append(3)
		else:
			y0 = 5/y0
			y0 = 8*y0
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