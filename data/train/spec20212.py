import numpy as np 

def function(x):

	c5 = 9
	y3 = 5
	paths = []
	try:
		if c5 <= 1:
			y3 = 4*y3
			y3 = 3+y3
			c5 = 1+4
			paths.append(1)
		else:
			y3 = y3/5
			paths.append(2)
		if y3 > 4:
			y3 = 2+y3
			c5 = c5/y3
			x = x+8
			paths.append(3)
		else:
			y3 = c5+8
			x = 4/x
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c5 = x**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))