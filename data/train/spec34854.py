import numpy as np 

def function(x):

	v1 = x
	c8 = x
	paths = []
	try:
		if v1 <= 7:
			v1 = 5/7
			x = 1+x
			paths.append(1)
		else:
			v1 = v1/8
			v1 = 7*2
			paths.append(2)
		if c8 > 0:
			v1 = v1-8
			c8 = x+c8
			v1 = 8*c8
			paths.append(3)
		else:
			c8 = v1+x
			c8 = 3*5
			c8 = c8-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))