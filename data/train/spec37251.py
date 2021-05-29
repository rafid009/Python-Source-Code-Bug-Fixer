import numpy as np 

def function(x):

	y7 = 3
	c6 = 1
	paths = []
	try:
		if c6 > 3:
			c6 = c6/5
			y7 = 9/6
			paths.append(1)
		else:
			x = 9/x
			c6 = 6*7
			c6 = 1*c6
			paths.append(2)
		if x > 6:
			c6 = 4*c6
			x = 1+2
			x = x-8
			paths.append(3)
		else:
			y7 = y7+y7
			y7 = y7*x
			y7 = x-9
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))