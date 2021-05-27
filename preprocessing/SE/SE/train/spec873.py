import numpy as np 

def function(x):

	y3 = 7
	c5 = 7
	x = x
	paths = []
	try:
		if x <= 6:
			y3 = 8+y3
			paths.append(1)
		else:
			y3 = 2/y3
			x = 3*1
			c5 = 9-c5
			paths.append(2)
		if x >= 1:
			c5 = c5*1
			x = x/c5
			x = 2+c5
			paths.append(3)
		else:
			c5 = y3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))