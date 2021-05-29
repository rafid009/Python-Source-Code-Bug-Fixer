import numpy as np 

def function(x):

	c4 = 3
	q1 = x
	paths = []
	try:
		if x <= 5:
			c4 = c4*x
			paths.append(1)
		else:
			x = 1*8
			x = 0+6
			paths.append(2)
		if q1 > 4:
			c4 = c4*q1
			paths.append(3)
		else:
			c4 = q1-c4
			c4 = q1*c4
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		c4 = q1**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))