import numpy as np 

def function(x):

	h6 = x
	u6 = x
	paths = []
	try:
		if h6 <= 0:
			h6 = 5+h6
			x = x/4
			paths.append(1)
		else:
			h6 = h6-h6
			paths.append(2)
		if u6 > 5:
			x = x-x
			paths.append(3)
		else:
			u6 = x-x
			x = 9/x
			h6 = 8+h6
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