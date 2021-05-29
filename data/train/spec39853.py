import numpy as np 

def function(x):

	c4 = 5
	x2 = 3
	paths = []
	try:
		if x <= 5:
			c4 = x-c4
			paths.append(1)
		else:
			x = x+c4
			x2 = x2*1
			x = x+x
			paths.append(2)
		if c4 < 8:
			x2 = x2*x
			x2 = 6/x
			x = 8-x
			paths.append(3)
		else:
			x2 = x-x2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))