import numpy as np 

def function(x):

	c4 = x
	r0 = 4
	paths = []
	try:
		if x > 6:
			x = 0/x
			x = 6-x
			c4 = c4/c4
			paths.append(1)
		else:
			r0 = x-r0
			r0 = 5*8
			r0 = 0*x
			paths.append(2)
		if x >= 4:
			x = r0/9
			c4 = 7/c4
			paths.append(3)
		else:
			c4 = c4*5
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