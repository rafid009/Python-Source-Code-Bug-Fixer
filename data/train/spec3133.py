import numpy as np 

def function(x):

	c9 = 6
	l1 = x
	paths = []
	try:
		if l1 >= 7:
			l1 = 2-l1
			c9 = c9*x
			paths.append(1)
		else:
			c9 = c9-4
			l1 = 6*7
			x = x+x
			paths.append(2)
		if c9 <= 7:
			c9 = 3+c9
			l1 = 6*l1
			paths.append(3)
		else:
			x = x-5
			c9 = 1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))