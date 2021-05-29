import numpy as np 

def function(x):

	c3 = x
	y2 = 5
	paths = []
	try:
		if c3 > 6:
			y2 = 3+x
			y2 = y2*3
			paths.append(1)
		else:
			y2 = 5-y2
			x = x-2
			c3 = 8/c3
			paths.append(2)
		if y2 >= 4:
			c3 = y2*y2
			x = 6*y2
			x = 4+c3
			paths.append(3)
		else:
			x = x-c3
			x = 7*x
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