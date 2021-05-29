import numpy as np 

def function(x):

	c2 = 4
	e1 = x
	paths = []
	try:
		if x > 7:
			c2 = 6+c2
			e1 = 9/x
			paths.append(1)
		else:
			x = c2+e1
			paths.append(2)
		if e1 < 3:
			x = c2/x
			paths.append(3)
		else:
			c2 = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))