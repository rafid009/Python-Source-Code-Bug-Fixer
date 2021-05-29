import numpy as np 

def function(x):

	c9 = 3
	f2 = 4
	paths = []
	try:
		if f2 < 0:
			f2 = 6+1
			x = 7+x
			c9 = 3+f2
			paths.append(1)
		else:
			x = c9-x
			paths.append(2)
		if f2 < 0:
			c9 = 4/c9
			paths.append(3)
		else:
			f2 = f2/x
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