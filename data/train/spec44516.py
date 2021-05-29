import numpy as np 

def function(x):

	y2 = 4
	c4 = x
	paths = []
	try:
		if y2 < 8:
			y2 = x/y2
			y2 = 8/1
			x = 6*x
			paths.append(1)
		else:
			x = 7/x
			c4 = x*c4
			x = x-x
			paths.append(2)
		if x <= 7:
			c4 = c4/1
			c4 = c4*c4
			paths.append(3)
		else:
			c4 = 6+c4
			c4 = 4+7
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