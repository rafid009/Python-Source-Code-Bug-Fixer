import numpy as np 

def function(x):

	x4 = 5
	c2 = x
	paths = []
	try:
		if c2 >= 4:
			x = x/8
			x4 = 9+1
			x = x/5
			paths.append(1)
		else:
			c2 = c2/2
			c2 = c2+1
			x = x-c2
			paths.append(2)
		if x4 >= 2:
			x4 = 8/c2
			paths.append(3)
		else:
			c2 = c2-6
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))