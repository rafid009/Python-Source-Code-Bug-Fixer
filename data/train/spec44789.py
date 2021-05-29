import numpy as np 

def function(x):

	c6 = x
	b0 = x
	paths = []
	try:
		if c6 < 1:
			b0 = b0*1
			x = 1-x
			x = 0-1
			paths.append(1)
		else:
			b0 = b0/2
			c6 = c6+8
			c6 = c6*c6
			paths.append(2)
		if b0 >= 3:
			b0 = 6*b0
			x = x+2
			c6 = 3+8
			paths.append(3)
		else:
			c6 = c6+5
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))