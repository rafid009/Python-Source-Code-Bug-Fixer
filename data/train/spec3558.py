import numpy as np 

def function(x):

	c6 = 7
	f4 = 1
	paths = []
	try:
		if f4 <= 7:
			f4 = 9*f4
			c6 = c6*c6
			paths.append(1)
		else:
			x = 6-x
			c6 = 2-7
			x = x+f4
			paths.append(2)
		if x > 4:
			x = x-7
			f4 = f4-c6
			paths.append(3)
		else:
			c6 = 8/f4
			x = 6*c6
			f4 = f4+6
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		c6 = f4**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))