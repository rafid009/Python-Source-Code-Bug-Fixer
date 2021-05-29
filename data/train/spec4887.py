import numpy as np 

def function(x):

	c1 = x
	y4 = 5
	paths = []
	try:
		if x >= 8:
			c1 = 5*4
			c1 = c1*3
			paths.append(1)
		else:
			y4 = 5+x
			y4 = 6*y4
			paths.append(2)
		if y4 >= 5:
			c1 = 2+0
			c1 = c1*y4
			x = 8/x
			paths.append(3)
		else:
			y4 = 6/y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))