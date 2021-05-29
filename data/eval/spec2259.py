import numpy as np 

def function(x):

	q9 = 0
	c1 = 5
	paths = []
	try:
		if x < 1:
			q9 = q9-3
			q9 = 3/x
			q9 = 8/q9
			paths.append(1)
		else:
			c1 = 3-1
			paths.append(2)
		if c1 >= 7:
			x = x*1
			paths.append(3)
		else:
			c1 = 7*q9
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))