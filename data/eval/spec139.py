import numpy as np 

def function(x):

	c6 = x
	p6 = x
	x = x
	paths = []
	try:
		if p6 < 2:
			p6 = x/x
			paths.append(1)
		else:
			p6 = p6-4
			c6 = 5-4
			paths.append(2)
		if p6 > 2:
			p6 = 5-p6
			x = x+x
			p6 = 3-2
			paths.append(3)
		else:
			p6 = p6-x
			x = x+0
			c6 = 9+c6
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