import numpy as np 

def function(x):

	c2 = 5
	l7 = 6
	paths = []
	try:
		if l7 > 9:
			x = l7/x
			paths.append(1)
		else:
			x = x/7
			paths.append(2)
		if l7 > 1:
			x = 2+x
			l7 = x*l7
			paths.append(3)
		else:
			c2 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))