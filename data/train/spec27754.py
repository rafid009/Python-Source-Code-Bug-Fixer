import numpy as np 

def function(x):

	p1 = 7
	c1 = x
	paths = []
	try:
		if p1 > 2:
			c1 = 6+x
			paths.append(1)
		else:
			p1 = 4/p1
			c1 = c1/p1
			paths.append(2)
		if p1 > 0:
			p1 = p1*x
			x = c1+c1
			x = x+c1
			paths.append(3)
		else:
			c1 = c1-3
			c1 = x*x
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