import numpy as np 

def function(x):

	i5 = x
	c0 = 7
	paths = []
	try:
		if c0 < 7:
			x = x*c0
			c0 = 0/c0
			x = x-2
			paths.append(1)
		else:
			x = i5*9
			paths.append(2)
		if i5 <= 1:
			c0 = 0*c0
			c0 = 0/3
			i5 = c0+i5
			paths.append(3)
		else:
			c0 = c0+4
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		c0 = i5**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))