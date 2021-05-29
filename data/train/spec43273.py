import numpy as np 

def function(x):

	a1 = x
	c0 = 8
	paths = []
	try:
		if a1 > 5:
			c0 = 0/c0
			x = 5-x
			paths.append(1)
		else:
			a1 = x+4
			x = x*6
			paths.append(2)
		if a1 >= 0:
			x = c0/7
			x = 9+c0
			paths.append(3)
		else:
			a1 = 4*a1
			c0 = 6*x
			a1 = x/7
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))