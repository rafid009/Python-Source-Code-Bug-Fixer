import numpy as np 

def function(x):

	i1 = 9
	c1 = x
	paths = []
	try:
		if c1 <= 6:
			i1 = i1-7
			i1 = 5*i1
			c1 = c1-5
			paths.append(1)
		else:
			i1 = 2+i1
			x = i1-9
			paths.append(2)
		if i1 > 1:
			i1 = i1-9
			paths.append(3)
		else:
			i1 = 8*i1
			x = 6/4
			i1 = c1*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c1 = x**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))