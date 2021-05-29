import numpy as np 

def function(x):

	f0 = 5
	c9 = 2
	paths = []
	try:
		if x < 0:
			x = f0-f0
			paths.append(1)
		else:
			c9 = c9*9
			paths.append(2)
		if f0 > 6:
			x = 5/6
			f0 = x+f0
			paths.append(3)
		else:
			c9 = c9-3
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))