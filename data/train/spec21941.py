import numpy as np 

def function(x):

	c4 = 9
	x2 = x
	paths = []
	try:
		if x > 5:
			c4 = x/2
			c4 = 7-c4
			x = x/3
			paths.append(1)
		else:
			x = 1/x
			x2 = x2-7
			x = x+x2
			paths.append(2)
		if x > 1:
			x2 = x2*3
			x2 = 9-1
			c4 = 5*c4
			paths.append(3)
		else:
			x2 = x2-2
			x2 = c4-3
			c4 = 2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))