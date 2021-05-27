import numpy as np 

def function(x):

	a9 = x
	c8 = 2
	paths = []
	try:
		if a9 > 3:
			c8 = 8/c8
			x = 2+x
			c8 = 9+8
			paths.append(1)
		else:
			x = 5*8
			x = x/1
			a9 = 0/4
			paths.append(2)
		if x > 9:
			c8 = c8+x
			c8 = 1-8
			a9 = a9*5
			paths.append(3)
		else:
			x = 1*1
			x = x-8
			c8 = c8-6
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