import numpy as np 

def function(x):

	h3 = 3
	c2 = x
	paths = []
	try:
		if c2 <= 6:
			x = x+7
			h3 = 8/c2
			c2 = c2+6
			paths.append(1)
		else:
			c2 = 4+c2
			paths.append(2)
		if h3 >= 4:
			c2 = c2+c2
			h3 = h3/x
			x = 5-h3
			paths.append(3)
		else:
			x = x*5
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))