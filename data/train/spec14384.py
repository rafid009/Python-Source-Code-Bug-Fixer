import numpy as np 

def function(x):

	h1 = 1
	a0 = x
	paths = []
	try:
		if x < 7:
			h1 = h1-h1
			a0 = a0-h1
			a0 = x+1
			paths.append(1)
		else:
			x = 8/4
			x = 0-x
			paths.append(2)
		if h1 < 7:
			a0 = a0+3
			h1 = h1*a0
			a0 = a0/5
			paths.append(3)
		else:
			h1 = 0-h1
			h1 = 8+4
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