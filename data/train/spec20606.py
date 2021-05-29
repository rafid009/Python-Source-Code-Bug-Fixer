import numpy as np 

def function(x):

	y3 = 9
	h0 = 0
	paths = []
	try:
		if x <= 8:
			h0 = h0+2
			paths.append(1)
		else:
			y3 = 9+3
			paths.append(2)
		if h0 >= 3:
			y3 = 0+9
			h0 = h0-h0
			x = x-7
			paths.append(3)
		else:
			x = 2/x
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