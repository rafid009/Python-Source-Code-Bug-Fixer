import numpy as np 

def function(x):

	c1 = 1
	n2 = x
	paths = []
	try:
		if n2 > 9:
			c1 = 1/1
			paths.append(1)
		else:
			c1 = 6-c1
			n2 = 4-n2
			n2 = n2*8
			paths.append(2)
		if c1 < 6:
			n2 = n2*c1
			paths.append(3)
		else:
			n2 = x-n2
			n2 = c1-x
			x = n2*x
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