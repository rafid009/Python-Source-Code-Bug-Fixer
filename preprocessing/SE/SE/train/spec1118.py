import numpy as np 

def function(x):

	c7 = 2
	j7 = x
	paths = []
	try:
		if x > 9:
			j7 = 0+j7
			c7 = c7-5
			j7 = 9+j7
			paths.append(1)
		else:
			c7 = 5+c7
			x = 3+x
			paths.append(2)
		if x > 2:
			x = 4/x
			x = x+2
			x = c7-1
			paths.append(3)
		else:
			c7 = j7*9
			x = 1*x
			x = x/x
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