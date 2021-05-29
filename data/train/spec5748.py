import numpy as np 

def function(x):

	c7 = x
	l9 = 5
	paths = []
	try:
		if x >= 5:
			l9 = l9/3
			x = 3+x
			paths.append(1)
		else:
			c7 = c7+4
			paths.append(2)
		if x <= 7:
			c7 = l9-3
			paths.append(3)
		else:
			c7 = 4*c7
			l9 = l9+5
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