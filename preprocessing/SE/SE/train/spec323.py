import numpy as np 

def function(x):

	h4 = 4
	n0 = 3
	paths = []
	try:
		if x <= 9:
			h4 = n0-5
			paths.append(1)
		else:
			n0 = n0/h4
			paths.append(2)
		if h4 < 0:
			h4 = h4/x
			paths.append(3)
		else:
			n0 = x/n0
			h4 = h4+h4
			x = x+h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))