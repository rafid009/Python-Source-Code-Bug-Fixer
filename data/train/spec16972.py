import numpy as np 

def function(x):

	o5 = x
	h1 = 9
	x = 1
	paths = []
	try:
		if h1 > 3:
			x = 3+o5
			h1 = x*h1
			h1 = 3/h1
			paths.append(1)
		else:
			h1 = 7+o5
			paths.append(2)
		if h1 < 2:
			h1 = h1-o5
			x = x+3
			h1 = o5/o5
			paths.append(3)
		else:
			x = x-4
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