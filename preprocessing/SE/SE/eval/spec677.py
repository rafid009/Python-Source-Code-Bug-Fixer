import numpy as np 

def function(x):

	h1 = x
	c6 = 0
	paths = []
	try:
		if h1 > 4:
			x = c6-x
			paths.append(1)
		else:
			h1 = h1+c6
			paths.append(2)
		if c6 >= 5:
			x = 2+8
			c6 = 2-c6
			h1 = x-0
			paths.append(3)
		else:
			x = 6+7
			c6 = 5-2
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		c6 = h1**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))