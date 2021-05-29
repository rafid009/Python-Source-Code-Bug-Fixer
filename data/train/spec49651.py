import numpy as np 

def function(x):

	c4 = x
	l1 = x
	paths = []
	try:
		if x <= 6:
			c4 = 3+2
			c4 = c4*2
			c4 = l1+5
			paths.append(1)
		else:
			c4 = c4+6
			c4 = c4+2
			paths.append(2)
		if c4 <= 3:
			x = x-c4
			paths.append(3)
		else:
			x = c4-x
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