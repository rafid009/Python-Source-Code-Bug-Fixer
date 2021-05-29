import numpy as np 

def function(x):

	u6 = 6
	h9 = 7
	paths = []
	try:
		if x > 7:
			x = 8*3
			h9 = 0*h9
			h9 = h9+h9
			paths.append(1)
		else:
			u6 = 9-u6
			x = x/h9
			paths.append(2)
		if u6 > 9:
			h9 = h9-5
			u6 = u6-7
			x = x*u6
			paths.append(3)
		else:
			h9 = h9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))