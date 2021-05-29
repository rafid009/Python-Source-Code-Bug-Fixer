import numpy as np 

def function(x):

	x5 = x
	h7 = 8
	paths = []
	try:
		if x >= 3:
			h7 = x5-h7
			paths.append(1)
		else:
			x5 = 5+2
			paths.append(2)
		if x5 >= 0:
			h7 = 1-2
			x = x*h7
			x5 = x5-5
			paths.append(3)
		else:
			x5 = 9+9
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		h7 = x5**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))