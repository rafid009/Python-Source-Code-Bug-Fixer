import numpy as np 

def function(x):

	n5 = x
	h4 = x
	paths = []
	try:
		if x <= 8:
			h4 = h4+3
			x = 6/x
			h4 = 0*h4
			paths.append(1)
		else:
			h4 = 8+4
			n5 = 4-n5
			paths.append(2)
		if x >= 6:
			h4 = h4-3
			paths.append(3)
		else:
			n5 = n5*h4
			h4 = h4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))