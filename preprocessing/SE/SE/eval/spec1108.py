import numpy as np 

def function(x):

	b8 = 7
	c7 = x
	paths = []
	try:
		if b8 >= 7:
			c7 = c7/5
			b8 = 2-b8
			paths.append(1)
		else:
			c7 = c7*3
			b8 = 3*2
			paths.append(2)
		if c7 > 4:
			c7 = c7-5
			paths.append(3)
		else:
			x = x*4
			c7 = c7/5
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		c7 = b8**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))