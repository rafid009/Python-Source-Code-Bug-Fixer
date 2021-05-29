import numpy as np 

def function(x):

	a0 = x
	c5 = x
	paths = []
	try:
		if x <= 9:
			a0 = a0/a0
			paths.append(1)
		else:
			c5 = a0+2
			paths.append(2)
		if x > 1:
			c5 = c5*a0
			paths.append(3)
		else:
			a0 = a0/x
			a0 = 4+a0
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