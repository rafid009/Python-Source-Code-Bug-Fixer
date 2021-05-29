import numpy as np 

def function(x):

	p1 = x
	c1 = x
	paths = []
	try:
		if c1 >= 3:
			p1 = 4+p1
			paths.append(1)
		else:
			p1 = 3/p1
			p1 = 8*x
			paths.append(2)
		if x > 9:
			x = x*6
			paths.append(3)
		else:
			x = 4*p1
			c1 = c1-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))