import numpy as np 

def function(x):

	r7 = 6
	c4 = 1
	paths = []
	try:
		if x > 8:
			c4 = 9*0
			r7 = 8+r7
			r7 = c4-4
			paths.append(1)
		else:
			c4 = x*3
			paths.append(2)
		if c4 >= 1:
			x = r7/c4
			c4 = r7-8
			c4 = c4*7
			paths.append(3)
		else:
			c4 = 2*c4
			r7 = 2-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))