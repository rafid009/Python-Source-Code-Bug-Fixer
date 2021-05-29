import numpy as np 

def function(x):

	h1 = 4
	a9 = x
	paths = []
	try:
		if x >= 6:
			x = 1*x
			x = a9-7
			a9 = a9+x
			paths.append(1)
		else:
			x = x-6
			a9 = 8/a9
			paths.append(2)
		if x >= 7:
			a9 = a9*8
			x = 6-x
			x = 5*x
			paths.append(3)
		else:
			h1 = h1/a9
			h1 = a9-6
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