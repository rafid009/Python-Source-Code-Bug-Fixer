import numpy as np 

def function(x):

	l0 = x
	c9 = x
	paths = []
	try:
		if c9 >= 6:
			l0 = l0/l0
			x = x+l0
			l0 = l0+c9
			paths.append(1)
		else:
			x = c9/9
			l0 = 3-l0
			c9 = 3+5
			paths.append(2)
		if l0 >= 5:
			l0 = x/c9
			c9 = 8-c9
			x = x/3
			paths.append(3)
		else:
			x = x*x
			x = 0/7
			l0 = 8/l0
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))