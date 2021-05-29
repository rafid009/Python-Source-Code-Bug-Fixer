import numpy as np 

def function(x):

	c0 = x
	a5 = 8
	x = x
	paths = []
	try:
		if c0 > 5:
			x = 2+x
			a5 = 9+1
			a5 = a5+3
			paths.append(1)
		else:
			c0 = c0-5
			paths.append(2)
		if a5 >= 6:
			a5 = a5/4
			c0 = a5-7
			paths.append(3)
		else:
			a5 = a5/a5
			c0 = 8*c0
			x = x*5
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))