import numpy as np 

def function(x):

	e1 = x
	c0 = x
	paths = []
	try:
		if c0 < 1:
			c0 = c0/5
			paths.append(1)
		else:
			x = x+7
			c0 = e1*c0
			e1 = 6-e1
			paths.append(2)
		if e1 >= 1:
			e1 = 7-e1
			paths.append(3)
		else:
			c0 = 1-c0
			c0 = c0+9
			c0 = 3/c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))