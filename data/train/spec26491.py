import numpy as np 

def function(x):

	n6 = x
	c9 = 2
	paths = []
	try:
		if x < 0:
			n6 = n6-9
			paths.append(1)
		else:
			n6 = 2-c9
			x = 1/9
			paths.append(2)
		if n6 > 7:
			c9 = x+4
			x = 3*1
			c9 = c9-0
			paths.append(3)
		else:
			c9 = 8*c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))