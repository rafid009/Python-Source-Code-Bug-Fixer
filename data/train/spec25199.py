import numpy as np 

def function(x):

	y3 = 9
	c4 = x
	paths = []
	try:
		if x >= 4:
			c4 = 5-y3
			x = 2/x
			paths.append(1)
		else:
			y3 = 5*6
			c4 = y3*c4
			paths.append(2)
		if c4 > 0:
			x = x+3
			paths.append(3)
		else:
			y3 = 3-7
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))