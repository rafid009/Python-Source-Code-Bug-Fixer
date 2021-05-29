import numpy as np 

def function(x):

	h7 = 3
	o2 = 3
	paths = []
	try:
		if h7 >= 2:
			h7 = 1-h7
			h7 = 3*h7
			paths.append(1)
		else:
			x = x+7
			h7 = 4+h7
			paths.append(2)
		if x >= 0:
			o2 = 8/o2
			h7 = h7-h7
			paths.append(3)
		else:
			x = 3-8
			h7 = 9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))