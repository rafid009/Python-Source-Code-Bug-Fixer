import numpy as np 

def function(x):

	c6 = x
	c5 = 8
	paths = []
	try:
		if c5 < 5:
			x = 2+4
			c6 = 9+c5
			x = 7/x
			paths.append(1)
		else:
			c5 = c5+2
			x = 8*x
			paths.append(2)
		if x < 6:
			c5 = 5+c5
			paths.append(3)
		else:
			x = x-3
			c5 = 4/2
			c6 = 2+c6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))