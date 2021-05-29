import numpy as np 

def function(x):

	c2 = 7
	i5 = 0
	paths = []
	try:
		if x > 3:
			c2 = 8/c2
			x = x+x
			i5 = x-1
			paths.append(1)
		else:
			c2 = c2*c2
			i5 = 3*c2
			c2 = 7+c2
			paths.append(2)
		if x <= 1:
			x = x+4
			c2 = c2*c2
			paths.append(3)
		else:
			c2 = x-i5
			x = 7-x
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