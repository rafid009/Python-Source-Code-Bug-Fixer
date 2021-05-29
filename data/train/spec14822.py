import numpy as np 

def function(x):

	c3 = x
	f5 = x
	paths = []
	try:
		if f5 >= 5:
			c3 = 3*c3
			paths.append(1)
		else:
			c3 = 9+7
			f5 = f5*9
			f5 = f5-1
			paths.append(2)
		if f5 >= 1:
			x = 1-x
			c3 = c3/c3
			c3 = c3*4
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		c3 = f5**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))