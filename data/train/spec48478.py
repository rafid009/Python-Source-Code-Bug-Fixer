import numpy as np 

def function(x):

	y5 = x
	h9 = 2
	paths = []
	try:
		if x < 6:
			h9 = y5*9
			y5 = h9-y5
			y5 = x+7
			paths.append(1)
		else:
			x = 4+1
			x = 3*y5
			h9 = h9+h9
			paths.append(2)
		if h9 <= 1:
			h9 = 7/h9
			paths.append(3)
		else:
			y5 = y5/3
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