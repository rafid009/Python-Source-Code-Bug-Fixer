import numpy as np 

def function(x):

	p8 = 1
	c9 = 1
	paths = []
	try:
		if p8 >= 5:
			p8 = x+p8
			x = p8*4
			p8 = p8/c9
			paths.append(1)
		else:
			c9 = c9-0
			paths.append(2)
		if x < 7:
			c9 = c9-4
			paths.append(3)
		else:
			x = c9/p8
			p8 = 9*p8
			c9 = x+c9
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