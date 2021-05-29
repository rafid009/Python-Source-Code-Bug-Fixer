import numpy as np 

def function(x):

	f4 = 4
	c9 = x
	paths = []
	try:
		if x < 9:
			f4 = 0-5
			c9 = x-c9
			x = 8+x
			paths.append(1)
		else:
			c9 = f4/x
			paths.append(2)
		if c9 < 5:
			c9 = c9-f4
			paths.append(3)
		else:
			x = 6-c9
			f4 = f4-2
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))