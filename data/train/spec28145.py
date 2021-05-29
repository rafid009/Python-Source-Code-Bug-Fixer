import numpy as np 

def function(x):

	y6 = 2
	c1 = 5
	paths = []
	try:
		if x <= 1:
			c1 = 0+c1
			c1 = x+2
			y6 = x-x
			paths.append(1)
		else:
			y6 = y6-3
			c1 = y6-7
			paths.append(2)
		if c1 <= 1:
			x = 3/x
			c1 = x*8
			y6 = 7-x
			paths.append(3)
		else:
			y6 = y6*2
			y6 = 1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))