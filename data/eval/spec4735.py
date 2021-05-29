import numpy as np 

def function(x):

	k7 = 1
	c6 = 0
	paths = []
	try:
		if k7 < 1:
			c6 = c6+1
			paths.append(1)
		else:
			x = x+5
			k7 = 4+6
			paths.append(2)
		if x <= 5:
			x = x+2
			paths.append(3)
		else:
			x = x+k7
			x = 4-k7
			c6 = k7+c6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c6 = x**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))