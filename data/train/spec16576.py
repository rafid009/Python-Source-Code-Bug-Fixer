import numpy as np 

def function(x):

	n2 = x
	c6 = 3
	paths = []
	try:
		if n2 >= 2:
			n2 = n2-9
			c6 = n2*3
			c6 = 5-c6
			paths.append(1)
		else:
			c6 = n2-x
			paths.append(2)
		if c6 >= 8:
			n2 = 8-x
			paths.append(3)
		else:
			c6 = c6+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))