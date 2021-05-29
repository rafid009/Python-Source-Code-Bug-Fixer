import numpy as np 

def function(x):

	l1 = 8
	c4 = 4
	paths = []
	try:
		if x <= 8:
			l1 = l1/5
			l1 = l1/c4
			paths.append(1)
		else:
			l1 = 3-5
			c4 = 9-l1
			x = x/x
			paths.append(2)
		if c4 >= 6:
			c4 = c4+x
			l1 = l1-8
			paths.append(3)
		else:
			l1 = 7*l1
			x = x/c4
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