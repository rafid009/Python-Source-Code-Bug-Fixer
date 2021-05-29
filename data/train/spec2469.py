import numpy as np 

def function(x):

	c2 = x
	a4 = 0
	paths = []
	try:
		if a4 <= 5:
			a4 = a4+9
			c2 = c2/a4
			paths.append(1)
		else:
			a4 = a4*9
			paths.append(2)
		if x > 2:
			c2 = 5*c2
			paths.append(3)
		else:
			x = x+9
			c2 = 2+c2
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