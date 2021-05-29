import numpy as np 

def function(x):

	c7 = 2
	d6 = x
	paths = []
	try:
		if c7 > 9:
			c7 = 0-c7
			d6 = 9*7
			x = x*5
			paths.append(1)
		else:
			x = c7*x
			paths.append(2)
		if x <= 4:
			x = 1+2
			c7 = x/9
			c7 = c7+c7
			paths.append(3)
		else:
			x = x-0
			c7 = d6-3
			c7 = c7-d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		c7 = d6**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))