import numpy as np 

def function(x):

	c3 = 8
	c0 = x
	paths = []
	try:
		if c3 > 9:
			c0 = 9-c0
			c0 = c0/6
			paths.append(1)
		else:
			c0 = c0-6
			x = 0*x
			paths.append(2)
		if c0 > 3:
			c0 = c3+0
			c3 = 4+c3
			x = x-c0
			paths.append(3)
		else:
			c0 = c0+1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))