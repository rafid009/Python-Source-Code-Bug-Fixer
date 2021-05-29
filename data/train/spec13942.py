import numpy as np 

def function(x):

	c0 = 1
	i8 = 4
	paths = []
	try:
		if i8 >= 9:
			c0 = 3+c0
			c0 = 0*6
			paths.append(1)
		else:
			i8 = c0-7
			c0 = c0+i8
			paths.append(2)
		if x > 7:
			i8 = x/3
			x = x-i8
			paths.append(3)
		else:
			x = i8/c0
			i8 = 4/i8
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