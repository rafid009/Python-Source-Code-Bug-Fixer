import numpy as np 

def function(x):

	g1 = x
	l4 = x
	paths = []
	try:
		if x > 3:
			l4 = l4*5
			l4 = g1*8
			x = l4/l4
			paths.append(1)
		else:
			x = g1+x
			paths.append(2)
		if x >= 1:
			l4 = 4+1
			l4 = l4-x
			l4 = g1/l4
			paths.append(3)
		else:
			g1 = g1+g1
			g1 = g1+l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))