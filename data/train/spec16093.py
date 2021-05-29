import numpy as np 

def function(x):

	r3 = x
	c9 = 2
	paths = []
	try:
		if x > 3:
			x = 0-7
			r3 = 0/r3
			paths.append(1)
		else:
			x = r3/8
			x = 9+r3
			paths.append(2)
		if x >= 9:
			r3 = 9/r3
			x = 7+x
			c9 = c9/3
			paths.append(3)
		else:
			c9 = x/c9
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