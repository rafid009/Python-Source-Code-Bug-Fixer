import numpy as np 

def function(x):

	y5 = 1
	c9 = x
	x = 3
	paths = []
	try:
		if x <= 8:
			y5 = y5+3
			paths.append(1)
		else:
			c9 = c9-7
			x = x-5
			paths.append(2)
		if x < 8:
			x = 7/x
			x = 9/x
			y5 = 4+x
			paths.append(3)
		else:
			c9 = 8+c9
			y5 = y5+3
			x = 6-9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))