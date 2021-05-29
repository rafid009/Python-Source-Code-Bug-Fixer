import numpy as np 

def function(x):

	l6 = x
	c1 = x
	paths = []
	try:
		if c1 >= 8:
			c1 = c1-4
			x = x/l6
			paths.append(1)
		else:
			l6 = c1/1
			paths.append(2)
		if l6 < 4:
			c1 = 7-9
			x = x-4
			l6 = x/l6
			paths.append(3)
		else:
			l6 = l6/1
			c1 = c1/x
			c1 = 4+c1
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))