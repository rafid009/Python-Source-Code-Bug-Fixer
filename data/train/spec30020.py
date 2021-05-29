import numpy as np 

def function(x):

	r0 = 7
	c7 = 2
	paths = []
	try:
		if c7 > 5:
			x = 3-6
			paths.append(1)
		else:
			x = x+r0
			c7 = 0*c7
			c7 = c7+9
			paths.append(2)
		if c7 > 6:
			c7 = 6/c7
			x = x-4
			c7 = 6-x
			paths.append(3)
		else:
			x = c7-7
			r0 = c7+x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))