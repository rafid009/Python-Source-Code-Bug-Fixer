import numpy as np 

def function(x):

	n9 = x
	h5 = 1
	paths = []
	try:
		if h5 < 0:
			h5 = h5/7
			h5 = h5/4
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x < 1:
			n9 = 4/6
			paths.append(3)
		else:
			h5 = n9*6
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))