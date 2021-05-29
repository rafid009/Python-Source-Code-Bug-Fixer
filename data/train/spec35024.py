import numpy as np 

def function(x):

	l0 = 3
	c3 = 2
	x = x
	paths = []
	try:
		if c3 >= 1:
			l0 = l0/2
			x = l0-x
			c3 = 2*1
			paths.append(1)
		else:
			c3 = 7/4
			c3 = c3-2
			paths.append(2)
		if l0 < 0:
			l0 = l0*x
			paths.append(3)
		else:
			c3 = 8/c3
			l0 = 6/6
			l0 = l0/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))