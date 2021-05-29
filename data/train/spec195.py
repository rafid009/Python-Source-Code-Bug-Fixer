import numpy as np 

def function(x):

	h5 = 9
	c9 = x
	paths = []
	try:
		if c9 > 0:
			x = 2/x
			c9 = x/1
			h5 = x-2
			paths.append(1)
		else:
			x = x+7
			h5 = 2+h5
			paths.append(2)
		if c9 > 3:
			c9 = 4*c9
			h5 = x+h5
			h5 = h5*5
			paths.append(3)
		else:
			c9 = 9+c9
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))