import numpy as np 

def function(x):

	p6 = x
	c6 = 1
	paths = []
	try:
		if c6 < 3:
			c6 = x*c6
			paths.append(1)
		else:
			p6 = c6-p6
			x = x-6
			paths.append(2)
		if p6 <= 6:
			c6 = 1*9
			paths.append(3)
		else:
			c6 = 7+5
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		c6 = p6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))