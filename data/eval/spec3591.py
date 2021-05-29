import numpy as np 

def function(x):

	y1 = x
	h9 = 3
	paths = []
	try:
		if y1 < 2:
			x = y1*x
			h9 = y1/4
			paths.append(1)
		else:
			h9 = 0*x
			paths.append(2)
		if y1 >= 0:
			x = 8-0
			h9 = h9*h9
			paths.append(3)
		else:
			h9 = 9*5
			y1 = y1+4
			h9 = 9*h9
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))