import numpy as np 

def function(x):

	g6 = x
	l6 = x
	paths = []
	try:
		if g6 <= 0:
			x = 9*g6
			g6 = x*g6
			g6 = g6/g6
			paths.append(1)
		else:
			l6 = x-g6
			paths.append(2)
		if l6 <= 8:
			l6 = 5+l6
			paths.append(3)
		else:
			g6 = g6-1
			g6 = g6+3
			g6 = g6-8
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