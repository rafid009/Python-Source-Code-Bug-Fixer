import numpy as np 

def function(x):

	p8 = 2
	c9 = 4
	paths = []
	try:
		if x < 0:
			p8 = p8*8
			p8 = c9+x
			paths.append(1)
		else:
			p8 = p8/c9
			p8 = p8+3
			p8 = 3-1
			paths.append(2)
		if x >= 6:
			c9 = c9-3
			c9 = c9-7
			paths.append(3)
		else:
			c9 = c9-x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))