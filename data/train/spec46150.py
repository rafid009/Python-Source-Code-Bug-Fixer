import numpy as np 

def function(x):

	n3 = 4
	h0 = 1
	paths = []
	try:
		if x > 8:
			h0 = 6+h0
			h0 = h0-2
			paths.append(1)
		else:
			h0 = 4*6
			paths.append(2)
		if h0 >= 6:
			n3 = n3/x
			paths.append(3)
		else:
			x = 8*h0
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))