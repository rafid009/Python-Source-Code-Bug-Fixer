import numpy as np 

def function(x):

	c7 = 8
	e3 = x
	paths = []
	try:
		if c7 >= 6:
			e3 = e3+c7
			paths.append(1)
		else:
			e3 = 4+e3
			e3 = 1+x
			c7 = c7/4
			paths.append(2)
		if c7 <= 0:
			e3 = c7/e3
			x = 3+x
			x = c7-x
			paths.append(3)
		else:
			c7 = 0/x
			c7 = c7/e3
			x = x/1
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		c7 = e3**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))