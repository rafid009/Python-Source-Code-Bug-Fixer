import numpy as np 

def function(x):

	e1 = x
	c4 = 4
	x = x
	paths = []
	try:
		if c4 >= 8:
			e1 = 6/e1
			x = x-8
			paths.append(1)
		else:
			x = c4+x
			c4 = c4*6
			c4 = e1-e1
			paths.append(2)
		if c4 <= 6:
			c4 = 7-c4
			e1 = 7/e1
			c4 = 5+5
			paths.append(3)
		else:
			x = 2/e1
			x = c4/x
			e1 = x/2
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))