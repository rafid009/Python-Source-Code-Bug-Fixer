import numpy as np 

def function(x):

	y2 = x
	c8 = x
	paths = []
	try:
		if c8 < 5:
			c8 = c8-5
			y2 = 8*9
			x = 4-6
			paths.append(1)
		else:
			c8 = x-c8
			c8 = c8*1
			c8 = 9-c8
			paths.append(2)
		if y2 >= 3:
			y2 = 3*y2
			y2 = y2+x
			paths.append(3)
		else:
			y2 = y2/8
			c8 = 6/4
			y2 = c8/1
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