import numpy as np 

def function(x):

	e7 = x
	h1 = 1
	paths = []
	try:
		if e7 >= 2:
			h1 = 1*h1
			x = 2*x
			e7 = e7-6
			paths.append(1)
		else:
			e7 = h1-4
			h1 = 7*e7
			paths.append(2)
		if e7 > 2:
			h1 = 9-3
			paths.append(3)
		else:
			h1 = h1/7
			h1 = h1-h1
			x = 7*5
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		h1 = e7**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))