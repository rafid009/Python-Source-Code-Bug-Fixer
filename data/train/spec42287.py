import numpy as np 

def function(x):

	c5 = 5
	i1 = x
	paths = []
	try:
		if c5 > 9:
			c5 = c5*5
			i1 = 7-i1
			x = i1-x
			paths.append(1)
		else:
			i1 = 9+i1
			x = i1/x
			paths.append(2)
		if c5 <= 0:
			x = x/5
			paths.append(3)
		else:
			c5 = x/c5
			x = 6/x
			i1 = i1-1
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