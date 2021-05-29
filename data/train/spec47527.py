import numpy as np 

def function(x):

	c5 = x
	x4 = x
	paths = []
	try:
		if x4 > 3:
			x = x+5
			x4 = c5*7
			paths.append(1)
		else:
			x = 3-6
			paths.append(2)
		if c5 >= 1:
			c5 = x*3
			c5 = 6+c5
			paths.append(3)
		else:
			x4 = 0+x
			c5 = c5-3
			c5 = c5*3
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))