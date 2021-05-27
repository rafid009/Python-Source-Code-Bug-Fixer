import numpy as np 

def function(x):

	j6 = 9
	c7 = x
	paths = []
	try:
		if c7 <= 9:
			x = 2/x
			x = 8-x
			c7 = j6*j6
			paths.append(1)
		else:
			j6 = j6+8
			j6 = j6+4
			x = 6/3
			paths.append(2)
		if x <= 2:
			c7 = c7*7
			j6 = j6-2
			j6 = x/j6
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))