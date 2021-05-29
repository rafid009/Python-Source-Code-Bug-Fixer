import numpy as np 

def function(x):

	n2 = x
	h3 = x
	paths = []
	try:
		if h3 <= 5:
			x = 3+2
			n2 = 2*n2
			paths.append(1)
		else:
			h3 = h3+6
			paths.append(2)
		if h3 < 0:
			h3 = 8/5
			x = 0-h3
			paths.append(3)
		else:
			h3 = h3+2
			x = 0-9
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		n2 = n2**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))