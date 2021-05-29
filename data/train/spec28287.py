import numpy as np 

def function(x):

	p4 = x
	c5 = x
	paths = []
	try:
		if c5 <= 7:
			x = x*6
			x = 3/x
			paths.append(1)
		else:
			x = 6*3
			paths.append(2)
		if c5 < 2:
			x = c5*8
			p4 = p4+8
			paths.append(3)
		else:
			c5 = c5/c5
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