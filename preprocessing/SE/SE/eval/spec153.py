import numpy as np 

def function(x):

	o4 = x
	c6 = 0
	paths = []
	try:
		if x > 0:
			c6 = x*c6
			o4 = x-x
			paths.append(1)
		else:
			o4 = 9*4
			x = x+1
			c6 = c6*4
			paths.append(2)
		if x < 4:
			o4 = o4*2
			o4 = 8/1
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))