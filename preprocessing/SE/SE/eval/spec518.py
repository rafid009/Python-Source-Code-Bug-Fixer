import numpy as np 

def function(x):

	c2 = 7
	i4 = x
	paths = []
	try:
		if x < 3:
			i4 = i4*5
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if c2 >= 4:
			x = x*1
			paths.append(3)
		else:
			i4 = c2-9
			i4 = c2-7
			x = 0-x
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