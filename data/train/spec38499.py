import numpy as np 

def function(x):

	p6 = x
	h6 = 5
	paths = []
	try:
		if h6 > 1:
			p6 = 5*9
			paths.append(1)
		else:
			h6 = 4-h6
			paths.append(2)
		if p6 < 2:
			h6 = h6/x
			h6 = 5/h6
			p6 = 9/5
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))