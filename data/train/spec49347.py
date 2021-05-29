import numpy as np 

def function(x):

	n2 = x
	h3 = 0
	paths = []
	try:
		if x > 0:
			n2 = h3*7
			x = 6*9
			paths.append(1)
		else:
			h3 = h3-7
			paths.append(2)
		if x > 2:
			h3 = h3-9
			paths.append(3)
		else:
			x = h3*x
			h3 = 5*n2
			x = x-2
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