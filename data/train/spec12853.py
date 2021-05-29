import numpy as np 

def function(x):

	c2 = 3
	v7 = 5
	paths = []
	try:
		if c2 <= 6:
			v7 = 5/x
			paths.append(1)
		else:
			v7 = v7*8
			c2 = 0+c2
			c2 = 8*c2
			paths.append(2)
		if v7 >= 9:
			c2 = 5+c2
			paths.append(3)
		else:
			v7 = 3/v7
			c2 = 6/c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))