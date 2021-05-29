import numpy as np 

def function(x):

	p4 = x
	c1 = x
	paths = []
	try:
		if c1 < 2:
			c1 = 0-c1
			paths.append(1)
		else:
			p4 = 3*p4
			c1 = p4*p4
			paths.append(2)
		if p4 < 9:
			p4 = x+4
			x = x/x
			p4 = x/p4
			paths.append(3)
		else:
			x = p4-6
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))