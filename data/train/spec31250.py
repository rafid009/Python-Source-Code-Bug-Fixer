import numpy as np 

def function(x):

	x9 = 2
	c5 = x
	paths = []
	try:
		if c5 < 6:
			x9 = 1+x9
			paths.append(1)
		else:
			c5 = c5*2
			x = x/2
			paths.append(2)
		if x >= 5:
			c5 = 4-c5
			c5 = 4+c5
			paths.append(3)
		else:
			c5 = 5+x
			x9 = c5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x9 = x**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))