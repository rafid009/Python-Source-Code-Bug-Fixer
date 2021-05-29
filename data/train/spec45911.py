import numpy as np 

def function(x):

	g7 = 6
	l3 = x
	paths = []
	try:
		if l3 > 8:
			g7 = 9/4
			l3 = 2-l3
			paths.append(1)
		else:
			g7 = 5*g7
			g7 = 6+g7
			paths.append(2)
		if x > 0:
			g7 = g7*4
			g7 = 7*g7
			x = x-g7
			paths.append(3)
		else:
			l3 = 8*5
			g7 = 7-g7
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		g7 = l3**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))