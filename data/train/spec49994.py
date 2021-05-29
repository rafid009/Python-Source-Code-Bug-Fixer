import numpy as np 

def function(x):

	c1 = 5
	c9 = 8
	paths = []
	try:
		if c1 > 1:
			c9 = 7*5
			c9 = 4+c9
			c1 = x*9
			paths.append(1)
		else:
			x = 8+x
			x = x-c9
			c1 = c1+c9
			paths.append(2)
		if x <= 7:
			x = 5+4
			x = x*7
			paths.append(3)
		else:
			x = x-4
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c9 = c1**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))