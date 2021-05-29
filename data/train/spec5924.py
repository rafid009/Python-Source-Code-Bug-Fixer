import numpy as np 

def function(x):

	c0 = x
	f4 = 5
	paths = []
	try:
		if f4 > 9:
			c0 = x+f4
			paths.append(1)
		else:
			x = 6+x
			f4 = f4/5
			f4 = c0/x
			paths.append(2)
		if x >= 8:
			f4 = c0/2
			c0 = c0*1
			c0 = c0+2
			paths.append(3)
		else:
			x = x+8
			c0 = c0+0
			c0 = 8-c0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c0 = x**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))