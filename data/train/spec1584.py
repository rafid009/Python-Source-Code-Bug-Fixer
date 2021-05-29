import numpy as np 

def function(x):

	h4 = 0
	c8 = x
	paths = []
	try:
		if h4 > 3:
			c8 = c8/6
			paths.append(1)
		else:
			x = x/8
			h4 = 9-h4
			c8 = c8-3
			paths.append(2)
		if x < 9:
			c8 = c8+2
			paths.append(3)
		else:
			x = h4*3
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