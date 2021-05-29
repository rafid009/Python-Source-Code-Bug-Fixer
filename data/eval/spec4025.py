import numpy as np 

def function(x):

	x5 = 5
	h4 = 8
	paths = []
	try:
		if x5 > 8:
			h4 = 7+6
			h4 = 1/3
			paths.append(1)
		else:
			x5 = x+0
			paths.append(2)
		if x < 8:
			h4 = 4*5
			h4 = h4+7
			paths.append(3)
		else:
			x = 2/5
			h4 = x-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))