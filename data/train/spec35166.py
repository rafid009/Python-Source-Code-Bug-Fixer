import numpy as np 

def function(x):

	p6 = 8
	c0 = 8
	paths = []
	try:
		if x > 7:
			x = x-6
			p6 = 8*x
			p6 = 7-p6
			paths.append(1)
		else:
			p6 = x/p6
			paths.append(2)
		if c0 > 6:
			c0 = c0/8
			c0 = c0-1
			c0 = c0/2
			paths.append(3)
		else:
			p6 = p6+4
			c0 = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))