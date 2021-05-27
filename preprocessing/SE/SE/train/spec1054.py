import numpy as np 

def function(x):

	c0 = x
	y2 = x
	paths = []
	try:
		if y2 >= 5:
			x = 7*x
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if c0 >= 4:
			c0 = x+9
			x = c0/x
			c0 = 6/c0
			paths.append(3)
		else:
			x = 0-2
			c0 = c0-x
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		y2 = c0**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))