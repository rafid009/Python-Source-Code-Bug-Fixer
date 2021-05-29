import numpy as np 

def function(x):

	x7 = 8
	c1 = 4
	paths = []
	try:
		if x7 > 9:
			x7 = x7+6
			paths.append(1)
		else:
			c1 = x*4
			x = 2*c1
			paths.append(2)
		if x <= 4:
			x = x*5
			x7 = x7/x
			paths.append(3)
		else:
			x7 = 7*x7
			x = 4*x7
			x7 = x7+5
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))