import numpy as np 

def function(x):

	c1 = x
	p3 = x
	paths = []
	try:
		if p3 >= 0:
			x = 9/c1
			x = 0+5
			p3 = p3-p3
			paths.append(1)
		else:
			p3 = p3*4
			x = 6/p3
			c1 = c1+8
			paths.append(2)
		if x < 0:
			c1 = 4-c1
			x = x-8
			paths.append(3)
		else:
			c1 = p3-1
			c1 = c1/x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))