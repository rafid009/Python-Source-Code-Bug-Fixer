import numpy as np 

def function(x):

	y5 = 2
	c6 = 2
	paths = []
	try:
		if x > 9:
			y5 = 3*c6
			y5 = y5/2
			paths.append(1)
		else:
			y5 = 0+c6
			y5 = y5/x
			paths.append(2)
		if x <= 9:
			c6 = c6*x
			c6 = c6*5
			paths.append(3)
		else:
			c6 = 6*6
			y5 = y5+9
			y5 = c6+4
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))