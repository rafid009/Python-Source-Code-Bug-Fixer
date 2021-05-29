import numpy as np 

def function(x):

	c7 = 9
	a0 = x
	paths = []
	try:
		if a0 > 1:
			x = x-6
			x = x/5
			paths.append(1)
		else:
			a0 = a0*4
			c7 = c7/6
			paths.append(2)
		if c7 > 2:
			x = c7-x
			paths.append(3)
		else:
			c7 = c7/6
			x = x-x
			c7 = x/8
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))