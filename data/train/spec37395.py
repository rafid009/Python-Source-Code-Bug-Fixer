import numpy as np 

def function(x):

	c0 = x
	q3 = 6
	paths = []
	try:
		if x >= 7:
			x = 5*x
			x = q3/x
			c0 = c0+1
			paths.append(1)
		else:
			x = q3+x
			paths.append(2)
		if x < 2:
			c0 = c0+8
			q3 = c0/8
			c0 = q3-3
			paths.append(3)
		else:
			q3 = 0*6
			q3 = 2-q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))