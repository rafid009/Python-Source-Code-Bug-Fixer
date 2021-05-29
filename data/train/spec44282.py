import numpy as np 

def function(x):

	c0 = x
	f5 = 3
	paths = []
	try:
		if f5 < 8:
			c0 = c0/1
			c0 = 7*c0
			f5 = f5/x
			paths.append(1)
		else:
			c0 = c0-f5
			c0 = c0*1
			paths.append(2)
		if f5 < 4:
			f5 = 0/4
			c0 = c0-x
			c0 = c0+x
			paths.append(3)
		else:
			f5 = f5*c0
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