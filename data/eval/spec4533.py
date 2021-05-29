import numpy as np 

def function(x):

	p3 = x
	c7 = 3
	paths = []
	try:
		if c7 > 4:
			x = x-7
			paths.append(1)
		else:
			p3 = p3/9
			paths.append(2)
		if c7 > 6:
			p3 = p3+7
			paths.append(3)
		else:
			c7 = c7-p3
			x = x/c7
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		c7 = p3**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))