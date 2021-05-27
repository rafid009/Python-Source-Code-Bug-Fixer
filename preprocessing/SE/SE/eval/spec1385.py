import numpy as np 

def function(x):

	h8 = x
	x = 2
	paths = []
	try:
		if h8 > 9:
			x = 1*x
			x = 2-h8
			paths.append(1)
		else:
			h8 = h8*9
			paths.append(2)
		if h8 <= 6:
			h8 = h8*h8
			x = x-7
			h8 = h8/3
			paths.append(3)
		else:
			h8 = 8*8
			h8 = 2*h8
			x = 9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))