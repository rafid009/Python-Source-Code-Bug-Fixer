import numpy as np 

def function(x):

	a0 = 1
	c5 = 0
	paths = []
	try:
		if a0 < 5:
			a0 = x*6
			a0 = a0*5
			x = 4+5
			paths.append(1)
		else:
			a0 = 9/a0
			a0 = 4+x
			c5 = c5-2
			paths.append(2)
		if a0 < 6:
			c5 = a0*c5
			c5 = c5/x
			paths.append(3)
		else:
			x = x+a0
			x = 9+a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		c5 = a0**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))