import numpy as np 

def function(x):

	p0 = x
	c3 = x
	paths = []
	try:
		if c3 >= 7:
			x = p0/5
			p0 = p0+9
			p0 = 7+8
			paths.append(1)
		else:
			x = x*8
			p0 = p0/c3
			x = 8/x
			paths.append(2)
		if c3 <= 1:
			x = 7+x
			x = 8-x
			paths.append(3)
		else:
			c3 = c3-4
			p0 = p0-p0
			p0 = 4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))