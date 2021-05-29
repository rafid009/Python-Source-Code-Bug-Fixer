import numpy as np 

def function(x):

	c6 = 9
	q9 = x
	paths = []
	try:
		if q9 >= 5:
			c6 = 2-q9
			x = 8-x
			paths.append(1)
		else:
			c6 = c6/7
			paths.append(2)
		if c6 < 5:
			c6 = c6/6
			paths.append(3)
		else:
			q9 = 1+x
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