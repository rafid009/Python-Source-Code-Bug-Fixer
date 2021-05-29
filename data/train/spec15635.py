import numpy as np 

def function(x):

	b7 = x
	h8 = 5
	paths = []
	try:
		if h8 < 5:
			x = 2/x
			h8 = h8-8
			b7 = 2/6
			paths.append(1)
		else:
			b7 = 9*b7
			paths.append(2)
		if h8 > 9:
			x = x-7
			b7 = b7*b7
			paths.append(3)
		else:
			h8 = 1*h8
			x = x*6
			h8 = h8/4
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		h8 = b7**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))