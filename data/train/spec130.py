import numpy as np 

def function(x):

	c8 = 3
	p2 = x
	paths = []
	try:
		if c8 >= 2:
			c8 = p2-x
			p2 = x+c8
			p2 = p2-9
			paths.append(1)
		else:
			p2 = p2-6
			x = x*0
			paths.append(2)
		if x <= 6:
			p2 = p2*5
			paths.append(3)
		else:
			c8 = c8-3
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))