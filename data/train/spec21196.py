import numpy as np 

def function(x):

	e2 = x
	h7 = x
	paths = []
	try:
		if h7 <= 3:
			x = h7*6
			h7 = 4+h7
			paths.append(1)
		else:
			h7 = x*x
			h7 = 2*h7
			paths.append(2)
		if h7 > 6:
			h7 = x-h7
			x = x+2
			paths.append(3)
		else:
			h7 = 8*h7
			x = h7-x
			x = 6/x
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