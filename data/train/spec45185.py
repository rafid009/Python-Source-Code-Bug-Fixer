import numpy as np 

def function(x):

	c1 = x
	c5 = 4
	paths = []
	try:
		if c1 >= 5:
			x = x*8
			c5 = 8-c5
			paths.append(1)
		else:
			c1 = 8*9
			paths.append(2)
		if c5 < 7:
			x = x+5
			c5 = c5-2
			c5 = 1-c5
			paths.append(3)
		else:
			c1 = c1*8
			x = 2*2
			x = 9+5
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