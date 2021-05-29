import numpy as np 

def function(x):

	c1 = 0
	e6 = 1
	paths = []
	try:
		if x <= 8:
			x = x+0
			x = c1+x
			c1 = 6*c1
			paths.append(1)
		else:
			c1 = 3+9
			x = 2+8
			c1 = c1+c1
			paths.append(2)
		if x >= 3:
			e6 = c1-e6
			c1 = 2*7
			e6 = 5/e6
			paths.append(3)
		else:
			x = x+8
			c1 = x+8
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		c1 = e6**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))