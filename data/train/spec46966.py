import numpy as np 

def function(x):

	n7 = x
	c3 = 6
	paths = []
	try:
		if x <= 2:
			c3 = c3-3
			x = x+c3
			c3 = c3+6
			paths.append(1)
		else:
			c3 = n7+c3
			c3 = x+c3
			paths.append(2)
		if x < 2:
			x = x+x
			paths.append(3)
		else:
			n7 = n7*6
			c3 = 1-n7
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))