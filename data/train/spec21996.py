import numpy as np 

def function(x):

	c1 = 0
	f7 = 4
	paths = []
	try:
		if c1 >= 9:
			x = x-2
			f7 = 8/f7
			paths.append(1)
		else:
			f7 = 8-1
			x = 4-x
			paths.append(2)
		if c1 > 3:
			x = x-2
			x = x*7
			x = 4/x
			paths.append(3)
		else:
			f7 = x*2
			f7 = f7-c1
			c1 = f7*c1
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		c1 = f7**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))