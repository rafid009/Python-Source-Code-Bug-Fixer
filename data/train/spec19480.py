import numpy as np 

def function(x):

	c3 = 9
	a3 = x
	paths = []
	try:
		if x <= 8:
			a3 = a3/c3
			c3 = c3*x
			x = c3+8
			paths.append(1)
		else:
			a3 = a3*x
			c3 = 7/7
			c3 = c3/c3
			paths.append(2)
		if c3 <= 4:
			c3 = a3*a3
			paths.append(3)
		else:
			a3 = a3-x
			a3 = a3-7
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		c3 = a3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))