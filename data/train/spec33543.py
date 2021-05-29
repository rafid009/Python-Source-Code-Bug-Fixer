import numpy as np 

def function(x):

	c3 = x
	y2 = 3
	x = x
	paths = []
	try:
		if y2 < 6:
			y2 = 6/y2
			c3 = c3+9
			paths.append(1)
		else:
			c3 = 8-6
			c3 = c3/1
			paths.append(2)
		if y2 >= 9:
			y2 = 1+6
			y2 = 0/c3
			x = 2/c3
			paths.append(3)
		else:
			x = x*y2
			y2 = 4*y2
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))