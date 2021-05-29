import numpy as np 

def function(x):

	c6 = 1
	j7 = 7
	paths = []
	try:
		if x < 2:
			c6 = c6+c6
			x = 3/x
			paths.append(1)
		else:
			c6 = c6*7
			c6 = 2+c6
			j7 = j7/9
			paths.append(2)
		if c6 < 8:
			j7 = j7*9
			c6 = c6/7
			j7 = j7*6
			paths.append(3)
		else:
			j7 = 6+j7
			x = 3+j7
			j7 = x+c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))