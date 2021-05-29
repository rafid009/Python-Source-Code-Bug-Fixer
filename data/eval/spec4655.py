import numpy as np 

def function(x):

	h8 = x
	h1 = x
	paths = []
	try:
		if h1 >= 1:
			h8 = h8*h8
			x = 2*4
			x = h8-x
			paths.append(1)
		else:
			h8 = h8+5
			x = h1/x
			h1 = x+h1
			paths.append(2)
		if x >= 0:
			h8 = h8+3
			h1 = h1+9
			x = 1*h1
			paths.append(3)
		else:
			h8 = h8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))