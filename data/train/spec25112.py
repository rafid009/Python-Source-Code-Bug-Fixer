import numpy as np 

def function(x):

	p4 = 0
	c4 = 3
	paths = []
	try:
		if p4 >= 7:
			c4 = 1+7
			c4 = p4/7
			c4 = 3/2
			paths.append(1)
		else:
			p4 = p4/x
			p4 = p4*x
			c4 = 4+0
			paths.append(2)
		if x < 6:
			c4 = 8+x
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))