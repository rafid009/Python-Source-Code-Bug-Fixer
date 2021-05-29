import numpy as np 

def function(x):

	l3 = x
	c0 = 7
	paths = []
	try:
		if l3 <= 2:
			c0 = c0*x
			l3 = 8*l3
			c0 = l3+7
			paths.append(1)
		else:
			l3 = x*x
			x = x+7
			paths.append(2)
		if l3 <= 2:
			c0 = c0/1
			l3 = l3+3
			paths.append(3)
		else:
			x = c0/2
			c0 = c0+x
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		c0 = l3**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))