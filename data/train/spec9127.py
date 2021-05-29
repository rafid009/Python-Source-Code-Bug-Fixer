import numpy as np 

def function(x):

	c9 = 7
	l8 = 9
	paths = []
	try:
		if l8 < 3:
			x = l8/x
			c9 = l8/c9
			x = x/3
			paths.append(1)
		else:
			c9 = 3*4
			x = c9+x
			l8 = c9-3
			paths.append(2)
		if l8 > 2:
			x = 3+x
			l8 = 5-6
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))