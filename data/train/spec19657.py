import numpy as np 

def function(x):

	h5 = x
	c8 = x
	paths = []
	try:
		if h5 <= 0:
			x = 0*h5
			paths.append(1)
		else:
			c8 = 8+c8
			paths.append(2)
		if x > 5:
			x = x/7
			h5 = 5*h5
			c8 = 1*c8
			paths.append(3)
		else:
			x = 3/h5
			h5 = 0-h5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))