import numpy as np 

def function(x):

	c1 = 3
	l6 = x
	paths = []
	try:
		if c1 <= 0:
			x = x+9
			c1 = c1-x
			paths.append(1)
		else:
			x = c1-x
			c1 = c1+6
			paths.append(2)
		if l6 > 5:
			c1 = c1/6
			x = x/7
			paths.append(3)
		else:
			x = 1-x
			x = 8-x
			x = 5*l6
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