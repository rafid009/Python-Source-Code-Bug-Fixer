import numpy as np 

def function(x):

	k7 = 2
	c5 = x
	paths = []
	try:
		if k7 > 9:
			c5 = k7/c5
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if k7 > 4:
			x = x-c5
			paths.append(3)
		else:
			x = 3+x
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