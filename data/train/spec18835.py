import numpy as np 

def function(x):

	j7 = x
	c5 = 1
	paths = []
	try:
		if x >= 4:
			j7 = 6*5
			paths.append(1)
		else:
			c5 = j7*c5
			c5 = 1/c5
			j7 = j7/5
			paths.append(2)
		if c5 < 8:
			x = x-2
			c5 = c5+5
			paths.append(3)
		else:
			j7 = 9/j7
			j7 = 2*6
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