import numpy as np 

def function(x):

	c0 = 3
	h6 = x
	paths = []
	try:
		if h6 >= 8:
			x = 5-2
			h6 = h6+7
			paths.append(1)
		else:
			h6 = h6+1
			h6 = 8*4
			x = x-8
			paths.append(2)
		if h6 < 5:
			c0 = 6+c0
			c0 = c0+c0
			paths.append(3)
		else:
			h6 = 3+0
			c0 = c0-c0
			h6 = 0-h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))