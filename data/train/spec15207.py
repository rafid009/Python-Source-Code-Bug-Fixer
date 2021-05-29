import numpy as np 

def function(x):

	r8 = 1
	c7 = 0
	paths = []
	try:
		if c7 < 2:
			r8 = 1-7
			c7 = c7-4
			c7 = c7*6
			paths.append(1)
		else:
			r8 = r8-0
			x = 7*x
			r8 = r8-0
			paths.append(2)
		if c7 <= 5:
			r8 = r8*8
			c7 = 8+c7
			c7 = c7+x
			paths.append(3)
		else:
			x = x*3
			c7 = 1*c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))