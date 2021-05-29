import numpy as np 

def function(x):

	f4 = x
	h9 = x
	paths = []
	try:
		if h9 >= 0:
			x = 3/4
			paths.append(1)
		else:
			h9 = f4+h9
			h9 = h9-3
			h9 = x/9
			paths.append(2)
		if x > 0:
			f4 = f4/3
			f4 = f4*x
			paths.append(3)
		else:
			x = 0*x
			h9 = h9*6
			h9 = h9+h9
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		h9 = f4**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))