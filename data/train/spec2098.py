import numpy as np 

def function(x):

	h5 = 6
	n3 = x
	paths = []
	try:
		if x > 2:
			h5 = h5*h5
			h5 = h5-0
			n3 = n3*1
			paths.append(1)
		else:
			n3 = 2-n3
			n3 = n3-8
			paths.append(2)
		if x <= 2:
			x = x+3
			n3 = 8*n3
			paths.append(3)
		else:
			h5 = h5+n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))