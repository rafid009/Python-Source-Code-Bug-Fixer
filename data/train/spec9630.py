import numpy as np 

def function(x):

	c5 = x
	a9 = x
	paths = []
	try:
		if x <= 2:
			x = x*c5
			a9 = 3+a9
			c5 = 6/c5
			paths.append(1)
		else:
			c5 = a9/c5
			c5 = 0+4
			paths.append(2)
		if a9 <= 0:
			c5 = c5/4
			a9 = c5/7
			a9 = 3-3
			paths.append(3)
		else:
			a9 = 3*4
			a9 = a9/2
			x = 7*4
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