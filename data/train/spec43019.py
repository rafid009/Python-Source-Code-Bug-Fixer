import numpy as np 

def function(x):

	c3 = x
	l8 = 9
	paths = []
	try:
		if l8 < 7:
			c3 = 8/x
			l8 = l8/1
			paths.append(1)
		else:
			l8 = l8/c3
			paths.append(2)
		if c3 >= 8:
			l8 = 9+2
			paths.append(3)
		else:
			l8 = l8+c3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))