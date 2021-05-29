import numpy as np 

def function(x):

	p4 = 5
	c4 = x
	paths = []
	try:
		if x < 9:
			p4 = p4*3
			c4 = x*3
			paths.append(1)
		else:
			x = x*p4
			c4 = p4+7
			c4 = c4-8
			paths.append(2)
		if x > 6:
			c4 = x+x
			paths.append(3)
		else:
			x = 0/x
			x = c4+8
			p4 = 6+8
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))