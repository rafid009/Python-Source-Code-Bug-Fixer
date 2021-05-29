import numpy as np 

def function(x):

	y1 = x
	h1 = 6
	paths = []
	try:
		if h1 < 0:
			y1 = 9/h1
			paths.append(1)
		else:
			x = x*h1
			x = x-h1
			h1 = h1-2
			paths.append(2)
		if y1 >= 8:
			y1 = y1+5
			h1 = 7-h1
			h1 = 3/h1
			paths.append(3)
		else:
			h1 = 1*h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))