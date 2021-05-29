import numpy as np 

def function(x):

	c4 = x
	n7 = x
	paths = []
	try:
		if c4 <= 4:
			x = 0-x
			n7 = n7/7
			n7 = n7*c4
			paths.append(1)
		else:
			n7 = 8+x
			n7 = c4+n7
			c4 = 8+3
			paths.append(2)
		if n7 < 5:
			c4 = 7*c4
			n7 = 9-n7
			paths.append(3)
		else:
			c4 = c4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))