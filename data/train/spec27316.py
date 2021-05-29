import numpy as np 

def function(x):

	h3 = x
	x5 = x
	paths = []
	try:
		if x > 8:
			x = 4-x
			h3 = h3-x
			paths.append(1)
		else:
			h3 = h3-6
			paths.append(2)
		if x5 >= 3:
			h3 = h3/h3
			x5 = 5/x5
			paths.append(3)
		else:
			x5 = 6-x5
			h3 = h3-x
			x = x/x5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))