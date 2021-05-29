import numpy as np 

def function(x):

	c8 = 1
	j4 = x
	paths = []
	try:
		if c8 > 0:
			c8 = 1+x
			paths.append(1)
		else:
			c8 = c8*1
			c8 = c8+5
			paths.append(2)
		if x <= 8:
			c8 = 9+c8
			paths.append(3)
		else:
			x = j4+x
			j4 = 5*j4
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