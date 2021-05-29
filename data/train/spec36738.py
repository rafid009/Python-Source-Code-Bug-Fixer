import numpy as np 

def function(x):

	c9 = 0
	r1 = 3
	paths = []
	try:
		if x >= 5:
			x = c9+2
			r1 = 1-r1
			x = r1-1
			paths.append(1)
		else:
			r1 = 3*r1
			c9 = x-x
			paths.append(2)
		if x > 1:
			r1 = r1-5
			x = 9*x
			paths.append(3)
		else:
			c9 = c9+r1
			r1 = 3/r1
			c9 = r1/c9
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))