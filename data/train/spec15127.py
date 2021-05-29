import numpy as np 

def function(x):

	k2 = 5
	c7 = x
	paths = []
	try:
		if c7 <= 7:
			c7 = 3/5
			k2 = x-c7
			c7 = k2+k2
			paths.append(1)
		else:
			c7 = c7*k2
			c7 = k2+c7
			paths.append(2)
		if x <= 7:
			x = x/2
			paths.append(3)
		else:
			c7 = 7+k2
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))