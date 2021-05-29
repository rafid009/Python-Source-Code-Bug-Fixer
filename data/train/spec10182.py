import numpy as np 

def function(x):

	c2 = 5
	p6 = x
	paths = []
	try:
		if c2 >= 8:
			c2 = c2-0
			x = x*8
			paths.append(1)
		else:
			c2 = 6/c2
			x = 0-x
			paths.append(2)
		if p6 > 1:
			x = c2/2
			paths.append(3)
		else:
			c2 = c2-5
			p6 = p6+x
			p6 = p6*c2
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