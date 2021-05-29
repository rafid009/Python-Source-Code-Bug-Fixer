import numpy as np 

def function(x):

	c4 = x
	p8 = 5
	paths = []
	try:
		if c4 >= 6:
			p8 = c4+x
			paths.append(1)
		else:
			p8 = p8*7
			paths.append(2)
		if c4 < 0:
			c4 = x*p8
			p8 = 0-p8
			paths.append(3)
		else:
			x = p8*3
			p8 = p8/p8
			p8 = 9/7
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		p8 = c4**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))