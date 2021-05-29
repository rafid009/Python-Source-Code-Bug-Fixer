import numpy as np 

def function(x):

	e6 = x
	c4 = 5
	paths = []
	try:
		if x < 6:
			x = 3+x
			c4 = 8/2
			paths.append(1)
		else:
			c4 = 2+c4
			e6 = e6+0
			paths.append(2)
		if c4 >= 4:
			c4 = x+3
			e6 = 6*e6
			paths.append(3)
		else:
			e6 = c4-c4
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