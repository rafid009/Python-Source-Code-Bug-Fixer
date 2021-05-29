import numpy as np 

def function(x):

	c5 = 7
	r1 = 2
	paths = []
	try:
		if r1 <= 2:
			r1 = 1+r1
			r1 = x*r1
			c5 = c5/7
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if c5 >= 2:
			c5 = 1-x
			paths.append(3)
		else:
			r1 = 8-r1
			c5 = c5*c5
			c5 = 9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))