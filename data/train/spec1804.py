import numpy as np 

def function(x):

	c2 = 3
	c5 = 5
	paths = []
	try:
		if c5 >= 8:
			c2 = c2*0
			paths.append(1)
		else:
			x = c2+1
			paths.append(2)
		if c5 >= 9:
			c5 = 1+c5
			c5 = 0/c5
			c5 = c5+c5
			paths.append(3)
		else:
			x = 9*1
			x = c2-x
			c5 = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))