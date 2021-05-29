import numpy as np 

def function(x):

	c4 = x
	f7 = x
	paths = []
	try:
		if x >= 0:
			f7 = c4+f7
			f7 = 6/4
			c4 = 0*x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if c4 >= 3:
			c4 = c4-8
			c4 = 7+x
			x = 0*x
			paths.append(3)
		else:
			f7 = f7*f7
			f7 = f7-7
			x = x*f7
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