import numpy as np 

def function(x):

	g1 = 1
	l7 = x
	paths = []
	try:
		if l7 >= 9:
			x = x+l7
			g1 = x/g1
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if g1 <= 3:
			g1 = g1/9
			l7 = 4/l7
			l7 = l7-0
			paths.append(3)
		else:
			l7 = 3+4
			g1 = g1/l7
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