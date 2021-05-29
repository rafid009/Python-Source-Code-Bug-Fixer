import numpy as np 

def function(x):

	c5 = x
	j7 = x
	paths = []
	try:
		if c5 > 0:
			c5 = c5*3
			paths.append(1)
		else:
			c5 = c5*c5
			j7 = j7+4
			paths.append(2)
		if c5 >= 2:
			c5 = 3*7
			c5 = 7-1
			x = 8+c5
			paths.append(3)
		else:
			c5 = c5/5
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		c5 = j7**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))