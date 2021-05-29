import numpy as np 

def function(x):

	c7 = 4
	p8 = 4
	paths = []
	try:
		if x < 8:
			x = x-6
			c7 = 2*c7
			p8 = x/7
			paths.append(1)
		else:
			x = x/5
			p8 = p8+7
			paths.append(2)
		if c7 <= 3:
			c7 = c7-p8
			paths.append(3)
		else:
			c7 = 6/c7
			x = 2/x
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		c7 = p8**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))