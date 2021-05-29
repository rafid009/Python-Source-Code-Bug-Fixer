import numpy as np 

def function(x):

	c9 = x
	r8 = 1
	paths = []
	try:
		if c9 > 5:
			c9 = 9+c9
			r8 = r8*5
			x = x*6
			paths.append(1)
		else:
			c9 = c9*4
			paths.append(2)
		if c9 < 1:
			c9 = c9*2
			c9 = r8+5
			paths.append(3)
		else:
			x = x+1
			c9 = 2/7
			x = 2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))