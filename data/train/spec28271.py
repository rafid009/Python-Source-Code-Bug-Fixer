import numpy as np 

def function(x):

	c6 = x
	e1 = 0
	x = x
	paths = []
	try:
		if c6 < 9:
			e1 = x-e1
			paths.append(1)
		else:
			e1 = e1*5
			paths.append(2)
		if c6 <= 9:
			e1 = 9*e1
			c6 = c6+0
			paths.append(3)
		else:
			c6 = c6-3
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))