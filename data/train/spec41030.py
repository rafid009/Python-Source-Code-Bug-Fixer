import numpy as np 

def function(x):

	h3 = x
	k7 = 5
	paths = []
	try:
		if h3 <= 6:
			x = 3+x
			h3 = k7*x
			h3 = x-2
			paths.append(1)
		else:
			h3 = 9-h3
			h3 = h3-4
			paths.append(2)
		if h3 < 2:
			x = 1/x
			x = x*3
			paths.append(3)
		else:
			x = 4*x
			h3 = h3*9
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