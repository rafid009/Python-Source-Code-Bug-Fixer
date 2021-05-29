import numpy as np 

def function(x):

	c4 = x
	r8 = 3
	paths = []
	try:
		if c4 > 7:
			r8 = x+x
			c4 = 7-c4
			x = x+9
			paths.append(1)
		else:
			r8 = r8/6
			c4 = 6-c4
			paths.append(2)
		if r8 < 0:
			x = r8-5
			r8 = 5+x
			paths.append(3)
		else:
			x = x/9
			x = x*4
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