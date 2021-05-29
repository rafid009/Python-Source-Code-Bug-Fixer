import numpy as np 

def function(x):

	c4 = x
	x0 = x
	paths = []
	try:
		if x > 3:
			x = c4*9
			x = 2*x0
			x = x+c4
			paths.append(1)
		else:
			x = 9/x
			x0 = 7+4
			paths.append(2)
		if x0 <= 0:
			x = x/2
			paths.append(3)
		else:
			x = 7/x
			c4 = x/1
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