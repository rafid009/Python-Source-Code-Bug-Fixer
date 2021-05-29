import numpy as np 

def function(x):

	n1 = x
	h5 = x
	x = 8
	paths = []
	try:
		if x >= 1:
			h5 = 9*h5
			h5 = 1*h5
			paths.append(1)
		else:
			h5 = x+7
			n1 = 1/n1
			paths.append(2)
		if h5 <= 9:
			x = x/h5
			n1 = n1*6
			paths.append(3)
		else:
			h5 = 2-h5
			x = x-x
			h5 = 8+h5
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