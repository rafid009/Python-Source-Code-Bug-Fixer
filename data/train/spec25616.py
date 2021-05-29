import numpy as np 

def function(x):

	y6 = x
	c8 = 4
	x = 7
	paths = []
	try:
		if y6 < 9:
			y6 = 0+8
			c8 = 3+c8
			x = c8-1
			paths.append(1)
		else:
			y6 = y6/6
			y6 = y6+2
			paths.append(2)
		if y6 <= 5:
			x = 0*x
			y6 = y6+9
			x = x/1
			paths.append(3)
		else:
			y6 = 8*4
			y6 = 7-y6
			y6 = y6/4
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		c8 = y6**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))