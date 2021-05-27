import numpy as np 

def function(x):

	c5 = 0
	h3 = x
	paths = []
	try:
		if h3 > 4:
			x = 9/x
			c5 = c5*5
			c5 = c5-4
			paths.append(1)
		else:
			x = x+3
			c5 = 1*c5
			h3 = 7+5
			paths.append(2)
		if x > 5:
			x = 7+7
			c5 = 3+2
			paths.append(3)
		else:
			x = 7*x
			h3 = h3+1
			c5 = 5-c5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))