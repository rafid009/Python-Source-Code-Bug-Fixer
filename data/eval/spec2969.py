import numpy as np 

def function(x):

	c0 = 8
	p8 = 4
	paths = []
	try:
		if x > 9:
			x = x/4
			p8 = p8/x
			paths.append(1)
		else:
			c0 = x-0
			p8 = x*9
			paths.append(2)
		if c0 <= 8:
			p8 = 2+c0
			c0 = x/p8
			c0 = 1-x
			paths.append(3)
		else:
			x = 5-p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		x = p8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))