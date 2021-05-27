import numpy as np 

def function(x):

	h8 = 3
	n3 = x
	paths = []
	try:
		if h8 <= 8:
			n3 = 4+n3
			paths.append(1)
		else:
			x = x/n3
			n3 = 1-1
			x = 2/x
			paths.append(2)
		if n3 > 9:
			h8 = x-n3
			x = h8*x
			x = 0/3
			paths.append(3)
		else:
			h8 = h8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))