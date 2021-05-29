import numpy as np 

def function(x):

	c5 = x
	f4 = x
	paths = []
	try:
		if c5 > 8:
			f4 = f4*5
			c5 = c5/5
			x = x*0
			paths.append(1)
		else:
			c5 = c5-6
			paths.append(2)
		if c5 >= 3:
			x = 0-x
			paths.append(3)
		else:
			c5 = f4+4
			f4 = 0+f4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		c5 = f4**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))