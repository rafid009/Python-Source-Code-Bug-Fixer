import numpy as np 

def function(x):

	c8 = x
	v0 = 4
	paths = []
	try:
		if x > 1:
			c8 = 3+c8
			paths.append(1)
		else:
			v0 = 2-c8
			c8 = c8*0
			paths.append(2)
		if c8 < 5:
			v0 = v0-2
			c8 = c8/7
			c8 = 1+c8
			paths.append(3)
		else:
			v0 = c8+c8
			c8 = c8*c8
			v0 = c8/c8
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		c8 = v0**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))