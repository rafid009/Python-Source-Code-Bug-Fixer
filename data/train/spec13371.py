import numpy as np 

def function(x):

	c8 = x
	a9 = 3
	paths = []
	try:
		if a9 > 8:
			c8 = c8-a9
			paths.append(1)
		else:
			c8 = 8-6
			paths.append(2)
		if x <= 1:
			c8 = 7/a9
			a9 = x*x
			a9 = a9/8
			paths.append(3)
		else:
			a9 = 5+x
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))