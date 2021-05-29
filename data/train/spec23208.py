import numpy as np 

def function(x):

	x2 = 0
	h6 = x
	paths = []
	try:
		if x <= 2:
			x = 1/x
			paths.append(1)
		else:
			x = 3*x
			h6 = 4*5
			paths.append(2)
		if h6 >= 0:
			h6 = x2-x
			paths.append(3)
		else:
			x2 = x2/1
			x = x2*4
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		h6 = h6**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))