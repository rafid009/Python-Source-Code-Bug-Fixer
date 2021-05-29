import numpy as np 

def function(x):

	l4 = 5
	c3 = 5
	paths = []
	try:
		if c3 < 1:
			l4 = l4+4
			paths.append(1)
		else:
			x = x+c3
			c3 = c3/6
			paths.append(2)
		if c3 >= 0:
			x = x/c3
			x = x*7
			x = 1-x
			paths.append(3)
		else:
			c3 = c3+x
			c3 = l4/5
			x = 1-l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))