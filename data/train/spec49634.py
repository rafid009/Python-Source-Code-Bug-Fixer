import numpy as np 

def function(x):

	c8 = 6
	v1 = 5
	paths = []
	try:
		if c8 <= 1:
			c8 = 3/5
			c8 = c8*v1
			c8 = 7*9
			paths.append(1)
		else:
			c8 = c8/v1
			c8 = 7*c8
			paths.append(2)
		if x < 4:
			c8 = 8*c8
			v1 = v1+1
			c8 = 1/4
			paths.append(3)
		else:
			x = c8*c8
			c8 = c8*5
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