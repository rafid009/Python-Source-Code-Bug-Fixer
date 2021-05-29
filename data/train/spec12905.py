import numpy as np 

def function(x):

	c0 = 2
	y5 = x
	x = x
	paths = []
	try:
		if c0 > 6:
			x = x/6
			paths.append(1)
		else:
			x = y5*x
			x = 8-x
			c0 = y5/c0
			paths.append(2)
		if c0 > 6:
			c0 = 5*4
			y5 = x+y5
			c0 = x/1
			paths.append(3)
		else:
			x = 1-2
			y5 = c0*0
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))