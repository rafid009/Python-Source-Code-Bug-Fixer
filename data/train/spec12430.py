import numpy as np 

def function(x):

	p2 = 0
	c9 = x
	paths = []
	try:
		if x < 6:
			p2 = p2+p2
			c9 = c9+p2
			paths.append(1)
		else:
			p2 = p2*c9
			paths.append(2)
		if c9 < 4:
			p2 = 8-p2
			p2 = x-6
			paths.append(3)
		else:
			p2 = p2-c9
			x = c9-8
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))