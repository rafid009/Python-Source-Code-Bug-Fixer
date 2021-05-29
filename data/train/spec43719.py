import numpy as np 

def function(x):

	p9 = x
	c4 = 4
	paths = []
	try:
		if p9 >= 0:
			c4 = c4/8
			p9 = p9-0
			c4 = 9*c4
			paths.append(1)
		else:
			c4 = 0+c4
			c4 = 2/c4
			paths.append(2)
		if c4 > 9:
			c4 = c4*c4
			c4 = c4-0
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))