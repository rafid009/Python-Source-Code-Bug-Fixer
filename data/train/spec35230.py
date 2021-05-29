import numpy as np 

def function(x):

	c6 = 6
	y1 = 9
	paths = []
	try:
		if y1 < 5:
			c6 = c6-7
			c6 = 9-c6
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if c6 <= 2:
			y1 = y1-0
			c6 = 1*5
			y1 = 8*y1
			paths.append(3)
		else:
			y1 = 5*y1
			y1 = y1+x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))