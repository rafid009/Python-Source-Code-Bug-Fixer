import numpy as np 

def function(x):

	p7 = 1
	c2 = x
	paths = []
	try:
		if p7 <= 3:
			x = x/p7
			c2 = 9+x
			paths.append(1)
		else:
			c2 = c2-c2
			c2 = 6-c2
			c2 = 3+8
			paths.append(2)
		if p7 >= 0:
			p7 = x+p7
			p7 = p7*6
			paths.append(3)
		else:
			x = 7+x
			c2 = c2-0
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		c2 = p7**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))