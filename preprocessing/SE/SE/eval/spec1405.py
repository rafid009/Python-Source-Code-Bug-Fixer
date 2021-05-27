import numpy as np 

def function(x):

	p8 = x
	c9 = 6
	x = 2
	paths = []
	try:
		if x >= 2:
			x = p8*6
			paths.append(1)
		else:
			p8 = 4/p8
			p8 = 4-p8
			paths.append(2)
		if x < 2:
			p8 = p8/c9
			p8 = p8+5
			paths.append(3)
		else:
			p8 = p8-x
			c9 = p8-c9
			x = x-6
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		p8 = c9**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))