import numpy as np 

def function(x):

	c7 = x
	l7 = 2
	paths = []
	try:
		if x > 9:
			x = 1/8
			paths.append(1)
		else:
			c7 = 3+c7
			x = 7+5
			x = x/c7
			paths.append(2)
		if l7 < 5:
			x = x+1
			l7 = l7/l7
			paths.append(3)
		else:
			x = l7-x
			l7 = l7*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))