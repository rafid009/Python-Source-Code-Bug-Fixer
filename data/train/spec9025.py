import numpy as np 

def function(x):

	c7 = 8
	p1 = 6
	paths = []
	try:
		if c7 <= 2:
			c7 = c7/7
			paths.append(1)
		else:
			c7 = c7/p1
			paths.append(2)
		if x <= 0:
			c7 = x*c7
			x = 5/x
			c7 = 1+p1
			paths.append(3)
		else:
			c7 = 2-p1
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