import numpy as np 

def function(x):

	n1 = 3
	h8 = x
	paths = []
	try:
		if x >= 8:
			x = 3+n1
			h8 = h8/x
			n1 = n1+n1
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if h8 > 8:
			h8 = 6+h8
			x = x+6
			paths.append(3)
		else:
			h8 = 5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))