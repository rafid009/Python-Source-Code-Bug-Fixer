import numpy as np 

def function(x):

	n5 = x
	c6 = 5
	paths = []
	try:
		if c6 <= 4:
			c6 = 2/4
			x = 5-5
			paths.append(1)
		else:
			c6 = 8-7
			n5 = x*n5
			x = 9-x
			paths.append(2)
		if x > 2:
			x = 2*5
			paths.append(3)
		else:
			n5 = x+x
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