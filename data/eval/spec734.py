import numpy as np 

def function(x):

	n8 = 2
	h2 = 2
	x = x
	paths = []
	try:
		if h2 < 3:
			h2 = 3/h2
			paths.append(1)
		else:
			x = 1-4
			paths.append(2)
		if h2 > 6:
			n8 = n8*h2
			h2 = 5*3
			x = x+3
			paths.append(3)
		else:
			h2 = n8*h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))