import numpy as np 

def function(x):

	c0 = x
	p1 = 7
	paths = []
	try:
		if c0 > 0:
			c0 = c0+p1
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if x >= 1:
			p1 = p1*x
			c0 = x+3
			c0 = p1-8
			paths.append(3)
		else:
			c0 = c0+0
			p1 = p1+6
			p1 = x*4
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))