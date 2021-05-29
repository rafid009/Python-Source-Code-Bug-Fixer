import numpy as np 

def function(x):

	c3 = 6
	l1 = x
	paths = []
	try:
		if l1 < 2:
			c3 = 3*c3
			x = c3*6
			paths.append(1)
		else:
			x = 0-3
			l1 = x+c3
			paths.append(2)
		if l1 <= 3:
			c3 = c3+3
			paths.append(3)
		else:
			x = 4/c3
			x = x-x
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))