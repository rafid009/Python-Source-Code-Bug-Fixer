import numpy as np 

def function(x):

	l4 = x
	g1 = 3
	paths = []
	try:
		if l4 >= 4:
			g1 = g1/g1
			g1 = g1-g1
			x = 3/8
			paths.append(1)
		else:
			l4 = 1/l4
			paths.append(2)
		if l4 >= 2:
			x = 4*x
			g1 = g1+x
			x = 2-x
			paths.append(3)
		else:
			x = x-9
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		g1 = l4**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))