import numpy as np 

def function(x):

	l7 = x
	h5 = 5
	paths = []
	try:
		if h5 > 4:
			h5 = h5-h5
			l7 = x+l7
			paths.append(1)
		else:
			h5 = x-h5
			x = x+2
			paths.append(2)
		if x <= 6:
			x = x*x
			x = 2-x
			paths.append(3)
		else:
			l7 = 5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h5 = x**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))