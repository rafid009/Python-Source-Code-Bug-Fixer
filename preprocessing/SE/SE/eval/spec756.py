import numpy as np 

def function(x):

	c1 = 3
	e6 = 1
	paths = []
	try:
		if x < 6:
			c1 = c1+7
			c1 = c1*8
			c1 = c1+e6
			paths.append(1)
		else:
			x = x*2
			e6 = e6-2
			paths.append(2)
		if x >= 4:
			c1 = c1*8
			paths.append(3)
		else:
			c1 = 4*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))