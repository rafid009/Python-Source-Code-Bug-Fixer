import numpy as np 

def function(x):

	y1 = 6
	c4 = 9
	x = x
	paths = []
	try:
		if y1 <= 7:
			c4 = c4+1
			y1 = c4+y1
			paths.append(1)
		else:
			x = 3*c4
			y1 = 6/y1
			x = 8-x
			paths.append(2)
		if x >= 9:
			x = 8+x
			y1 = y1*2
			x = y1-x
			paths.append(3)
		else:
			x = 1*2
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))