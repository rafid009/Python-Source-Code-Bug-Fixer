import numpy as np 

def function(x):

	c1 = 9
	q3 = 3
	paths = []
	try:
		if c1 <= 9:
			x = x+1
			paths.append(1)
		else:
			c1 = 2+q3
			paths.append(2)
		if x < 7:
			q3 = q3-q3
			c1 = c1*q3
			paths.append(3)
		else:
			q3 = 9-q3
			x = q3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))