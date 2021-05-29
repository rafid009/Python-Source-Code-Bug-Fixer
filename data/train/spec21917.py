import numpy as np 

def function(x):

	p6 = 5
	c3 = 6
	paths = []
	try:
		if p6 >= 2:
			p6 = 2*p6
			paths.append(1)
		else:
			c3 = 6+3
			x = 4-4
			x = 5-p6
			paths.append(2)
		if p6 >= 8:
			c3 = x+9
			paths.append(3)
		else:
			p6 = 1/8
			c3 = c3+6
			c3 = c3-c3
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))