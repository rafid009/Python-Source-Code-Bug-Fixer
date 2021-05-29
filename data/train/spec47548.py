import numpy as np 

def function(x):

	c4 = 4
	l6 = 5
	x = x
	paths = []
	try:
		if x >= 6:
			c4 = c4-8
			paths.append(1)
		else:
			l6 = 4-9
			paths.append(2)
		if x < 7:
			c4 = 5*l6
			paths.append(3)
		else:
			x = 1/1
			c4 = c4+5
			l6 = 7-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))