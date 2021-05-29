import numpy as np 

def function(x):

	w0 = 1
	y7 = 8
	paths = []
	try:
		if y7 <= 0:
			y7 = y7+w0
			y7 = w0+5
			paths.append(1)
		else:
			y7 = 1-w0
			paths.append(2)
		if x >= 8:
			w0 = w0*y7
			paths.append(3)
		else:
			w0 = 3/8
			y7 = w0-y7
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))