import numpy as np 

def function(x):

	g4 = 3
	l7 = x
	paths = []
	try:
		if g4 < 3:
			l7 = 5+g4
			g4 = 4-2
			paths.append(1)
		else:
			l7 = g4-8
			paths.append(2)
		if l7 > 5:
			l7 = 8-l7
			paths.append(3)
		else:
			l7 = 9*l7
			g4 = g4*7
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		g4 = l7**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))