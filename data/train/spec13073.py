import numpy as np 

def function(x):

	q8 = x
	c2 = 1
	paths = []
	try:
		if x <= 1:
			c2 = c2+1
			x = 6*x
			c2 = 7/x
			paths.append(1)
		else:
			q8 = q8+0
			paths.append(2)
		if x > 3:
			q8 = q8*q8
			x = 9*7
			q8 = 2+c2
			paths.append(3)
		else:
			x = 5*x
			q8 = 1+c2
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