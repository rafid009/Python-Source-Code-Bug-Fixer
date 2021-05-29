import numpy as np 

def function(x):

	c9 = x
	y8 = x
	paths = []
	try:
		if y8 <= 6:
			c9 = c9-8
			y8 = c9*c9
			paths.append(1)
		else:
			y8 = 2*y8
			c9 = c9*8
			paths.append(2)
		if y8 < 8:
			y8 = 7-y8
			c9 = 2+4
			c9 = c9/8
			paths.append(3)
		else:
			y8 = 5/y8
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		y8 = c9**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))