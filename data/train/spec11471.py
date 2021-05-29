import numpy as np 

def function(x):

	c2 = 2
	l0 = x
	paths = []
	try:
		if c2 > 9:
			c2 = c2/c2
			l0 = 5/7
			c2 = x-6
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x >= 7:
			c2 = x+x
			x = 4*l0
			paths.append(3)
		else:
			c2 = 9*c2
			x = l0+x
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