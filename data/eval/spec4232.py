import numpy as np 

def function(x):

	n6 = x
	c4 = x
	paths = []
	try:
		if x < 4:
			x = x*x
			c4 = c4-7
			n6 = 1*n6
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if n6 <= 0:
			x = n6+x
			paths.append(3)
		else:
			x = x/7
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