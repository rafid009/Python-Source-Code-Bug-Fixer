import numpy as np 

def function(x):

	c6 = 6
	j9 = 7
	paths = []
	try:
		if x > 5:
			x = 2/x
			x = 3*j9
			paths.append(1)
		else:
			x = x+x
			c6 = 3*9
			paths.append(2)
		if c6 < 7:
			c6 = c6/6
			x = c6/x
			c6 = 1*3
			paths.append(3)
		else:
			c6 = c6*x
			j9 = 9+j9
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))