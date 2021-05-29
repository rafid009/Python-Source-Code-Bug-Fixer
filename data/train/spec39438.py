import numpy as np 

def function(x):

	a9 = x
	c0 = x
	paths = []
	try:
		if c0 <= 4:
			c0 = c0*x
			x = x/c0
			c0 = c0-6
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x >= 7:
			c0 = 9*c0
			x = x/c0
			paths.append(3)
		else:
			c0 = c0-0
			a9 = 0+a9
			a9 = x-5
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		a9 = c0**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))