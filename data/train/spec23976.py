import numpy as np 

def function(x):

	c1 = x
	e4 = 6
	paths = []
	try:
		if x >= 7:
			x = c1-0
			e4 = e4-9
			paths.append(1)
		else:
			e4 = 9-e4
			paths.append(2)
		if e4 < 6:
			e4 = 2/e4
			c1 = 7-c1
			e4 = 4-e4
			paths.append(3)
		else:
			e4 = e4*2
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