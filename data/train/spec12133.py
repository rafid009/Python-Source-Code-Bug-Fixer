import numpy as np 

def function(x):

	n0 = 4
	h9 = x
	paths = []
	try:
		if h9 > 0:
			n0 = n0-h9
			n0 = 8+n0
			x = x/6
			paths.append(1)
		else:
			n0 = 7*n0
			paths.append(2)
		if h9 <= 8:
			x = n0-x
			x = 1-x
			x = x*n0
			paths.append(3)
		else:
			x = 6+h9
			h9 = h9/1
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))