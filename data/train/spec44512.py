import numpy as np 

def function(x):

	i5 = 0
	c0 = 4
	paths = []
	try:
		if c0 > 3:
			c0 = 2-c0
			paths.append(1)
		else:
			c0 = i5*c0
			i5 = i5/i5
			paths.append(2)
		if x > 4:
			c0 = 3+c0
			x = x+c0
			i5 = 7/8
			paths.append(3)
		else:
			i5 = i5+i5
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))