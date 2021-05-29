import numpy as np 

def function(x):

	h7 = 7
	c9 = 8
	paths = []
	try:
		if x >= 8:
			x = 6*0
			c9 = x-7
			paths.append(1)
		else:
			h7 = h7-0
			c9 = c9+c9
			h7 = x-h7
			paths.append(2)
		if c9 <= 8:
			x = h7*0
			paths.append(3)
		else:
			x = c9*x
			h7 = 2+h7
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