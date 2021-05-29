import numpy as np 

def function(x):

	c0 = x
	f7 = 9
	x = x
	paths = []
	try:
		if x >= 4:
			x = x/2
			c0 = c0*c0
			paths.append(1)
		else:
			c0 = c0-2
			x = 4/x
			paths.append(2)
		if x <= 8:
			c0 = c0+7
			f7 = f7-0
			paths.append(3)
		else:
			c0 = 1+1
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