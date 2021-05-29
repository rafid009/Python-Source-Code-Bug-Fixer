import numpy as np 

def function(x):

	g9 = 2
	l7 = x
	paths = []
	try:
		if l7 >= 8:
			g9 = 4/g9
			l7 = x/l7
			g9 = 5+g9
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if g9 < 1:
			x = 7-x
			x = g9*g9
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))