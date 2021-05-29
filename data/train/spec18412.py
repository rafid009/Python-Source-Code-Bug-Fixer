import numpy as np 

def function(x):

	a0 = 2
	c6 = x
	paths = []
	try:
		if a0 >= 6:
			a0 = a0/7
			paths.append(1)
		else:
			a0 = a0-a0
			x = 3-x
			paths.append(2)
		if x >= 4:
			x = 0-4
			paths.append(3)
		else:
			a0 = a0-6
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