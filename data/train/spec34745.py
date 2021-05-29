import numpy as np 

def function(x):

	y4 = x
	h2 = x
	x = x
	paths = []
	try:
		if h2 <= 6:
			x = h2/4
			h2 = h2*h2
			h2 = 6*x
			paths.append(1)
		else:
			h2 = 4-y4
			x = x/y4
			paths.append(2)
		if x <= 9:
			x = x/4
			paths.append(3)
		else:
			h2 = h2/y4
			h2 = h2/2
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))