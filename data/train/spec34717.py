import numpy as np 

def function(x):

	c6 = 6
	a4 = 9
	paths = []
	try:
		if a4 > 6:
			c6 = c6*c6
			a4 = a4*2
			x = x-5
			paths.append(1)
		else:
			a4 = c6/a4
			paths.append(2)
		if c6 >= 9:
			c6 = c6-8
			x = 9/x
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))