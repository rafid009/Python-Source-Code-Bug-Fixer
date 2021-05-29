import numpy as np 

def function(x):

	l1 = x
	c0 = 2
	x = 6
	paths = []
	try:
		if c0 >= 4:
			x = 3/x
			x = x/3
			paths.append(1)
		else:
			x = c0/x
			x = x-7
			paths.append(2)
		if l1 >= 6:
			l1 = l1+5
			l1 = l1-l1
			paths.append(3)
		else:
			c0 = c0*x
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))