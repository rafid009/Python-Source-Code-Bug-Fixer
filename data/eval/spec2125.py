import numpy as np 

def function(x):

	b6 = 3
	c4 = x
	paths = []
	try:
		if b6 >= 0:
			x = 2/5
			paths.append(1)
		else:
			x = x*6
			x = 0/6
			paths.append(2)
		if x >= 4:
			c4 = 1+c4
			paths.append(3)
		else:
			c4 = c4-8
			x = c4+2
			b6 = x*b6
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))