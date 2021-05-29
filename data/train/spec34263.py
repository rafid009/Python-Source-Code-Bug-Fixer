import numpy as np 

def function(x):

	c8 = x
	f6 = x
	paths = []
	try:
		if x <= 5:
			x = x-3
			f6 = f6/x
			paths.append(1)
		else:
			x = 5+c8
			f6 = f6+1
			paths.append(2)
		if x < 6:
			x = x-9
			c8 = c8*5
			x = c8-x
			paths.append(3)
		else:
			f6 = 2-f6
			c8 = f6/c8
			x = x+c8
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		c8 = f6**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))