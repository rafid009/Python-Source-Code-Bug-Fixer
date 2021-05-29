import numpy as np 

def function(x):

	c9 = x
	h3 = x
	x = 4
	paths = []
	try:
		if h3 > 1:
			c9 = c9*x
			h3 = h3-8
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if c9 < 3:
			h3 = c9-8
			c9 = c9-0
			paths.append(3)
		else:
			h3 = h3-6
			c9 = x+1
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))