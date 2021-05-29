import numpy as np 

def function(x):

	c1 = 9
	g1 = x
	paths = []
	try:
		if g1 > 0:
			x = 2-x
			paths.append(1)
		else:
			c1 = 7/c1
			x = g1*x
			x = x-4
			paths.append(2)
		if x < 2:
			c1 = c1*c1
			paths.append(3)
		else:
			c1 = c1*g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))