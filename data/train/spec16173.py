import numpy as np 

def function(x):

	c7 = x
	x7 = 6
	paths = []
	try:
		if x >= 5:
			x = x/c7
			x7 = 6+x7
			x = 4/1
			paths.append(1)
		else:
			x7 = 6*c7
			paths.append(2)
		if x7 > 9:
			x7 = c7-2
			c7 = 7/5
			x = x-c7
			paths.append(3)
		else:
			x7 = x7*x7
			c7 = c7-c7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))