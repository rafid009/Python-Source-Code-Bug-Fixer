import numpy as np 

def function(x):

	c4 = 9
	p7 = x
	paths = []
	try:
		if p7 < 6:
			x = 4-5
			c4 = 2+p7
			c4 = 9/c4
			paths.append(1)
		else:
			p7 = 1/p7
			paths.append(2)
		if c4 < 6:
			x = 2*x
			c4 = c4+0
			paths.append(3)
		else:
			c4 = x+c4
			x = x-2
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		p7 = c4**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))