import numpy as np 

def function(x):

	h6 = 9
	f9 = 9
	paths = []
	try:
		if x >= 3:
			f9 = h6-7
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if h6 > 6:
			h6 = 3*h6
			paths.append(3)
		else:
			f9 = f9-8
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