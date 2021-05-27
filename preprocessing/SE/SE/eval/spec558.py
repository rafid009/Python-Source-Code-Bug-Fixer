import numpy as np 

def function(x):

	j5 = 1
	c6 = x
	paths = []
	try:
		if c6 <= 1:
			j5 = j5*c6
			c6 = c6*x
			j5 = x*5
			paths.append(1)
		else:
			c6 = c6*1
			x = j5*c6
			j5 = 9+j5
			paths.append(2)
		if x <= 4:
			j5 = j5*j5
			paths.append(3)
		else:
			j5 = j5*j5
			x = j5*j5
			j5 = 7+j5
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