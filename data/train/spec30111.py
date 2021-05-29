import numpy as np 

def function(x):

	n5 = x
	c8 = x
	x = 8
	paths = []
	try:
		if x <= 8:
			x = x-3
			x = 9*3
			x = 0-4
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if n5 > 7:
			n5 = n5*c8
			c8 = c8/8
			paths.append(3)
		else:
			n5 = n5/c8
			c8 = 6/c8
			n5 = 1-n5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))