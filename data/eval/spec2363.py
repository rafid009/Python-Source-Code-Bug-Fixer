import numpy as np 

def function(x):

	h9 = x
	q8 = x
	paths = []
	try:
		if h9 >= 6:
			h9 = h9-9
			h9 = h9+2
			paths.append(1)
		else:
			q8 = q8-x
			paths.append(2)
		if h9 < 2:
			q8 = h9/4
			paths.append(3)
		else:
			x = 1/x
			x = x-0
			x = x+4
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		x = h9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))