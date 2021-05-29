import numpy as np 

def function(x):

	c6 = x
	e6 = 5
	paths = []
	try:
		if c6 <= 3:
			x = 3-x
			paths.append(1)
		else:
			e6 = x/1
			x = 3/6
			c6 = e6*x
			paths.append(2)
		if x > 0:
			e6 = 3+8
			x = e6/c6
			x = x*c6
			paths.append(3)
		else:
			x = x/x
			x = x/3
			c6 = 1+c6
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