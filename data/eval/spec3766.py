import numpy as np 

def function(x):

	e3 = 8
	h9 = x
	paths = []
	try:
		if x > 0:
			x = 3-x
			x = x-h9
			paths.append(1)
		else:
			e3 = 3-5
			e3 = 2-4
			h9 = h9+8
			paths.append(2)
		if x >= 8:
			h9 = x+x
			paths.append(3)
		else:
			x = h9*4
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))