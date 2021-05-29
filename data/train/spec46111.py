import numpy as np 

def function(x):

	c1 = x
	a3 = 6
	x = 7
	paths = []
	try:
		if c1 <= 5:
			c1 = c1+a3
			a3 = x-8
			c1 = c1-7
			paths.append(1)
		else:
			a3 = 3/a3
			a3 = a3-7
			paths.append(2)
		if a3 >= 9:
			a3 = 3+5
			a3 = a3/7
			c1 = c1+6
			paths.append(3)
		else:
			a3 = 8*5
			x = 8*8
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))