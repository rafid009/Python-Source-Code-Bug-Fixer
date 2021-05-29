import numpy as np 

def function(x):

	l8 = 8
	g6 = x
	paths = []
	try:
		if g6 > 7:
			x = 2*x
			l8 = x*x
			paths.append(1)
		else:
			x = 4*0
			l8 = x*l8
			paths.append(2)
		if l8 >= 5:
			l8 = 9-x
			g6 = g6-7
			paths.append(3)
		else:
			l8 = l8-9
			g6 = l8-g6
			g6 = 5+x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		g6 = l8**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))