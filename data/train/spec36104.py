import numpy as np 

def function(x):

	h8 = x
	e4 = 0
	paths = []
	try:
		if h8 > 0:
			e4 = 5+h8
			paths.append(1)
		else:
			e4 = 1*4
			e4 = e4/8
			paths.append(2)
		if h8 > 7:
			h8 = h8*5
			x = 3+e4
			paths.append(3)
		else:
			e4 = 7-e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		h8 = e4**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))