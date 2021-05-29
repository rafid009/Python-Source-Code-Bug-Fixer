import numpy as np 

def function(x):

	n9 = x
	c4 = 1
	paths = []
	try:
		if n9 > 3:
			x = n9+4
			paths.append(1)
		else:
			n9 = n9*4
			paths.append(2)
		if n9 <= 1:
			c4 = x+6
			paths.append(3)
		else:
			n9 = n9+0
			c4 = 1+c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))