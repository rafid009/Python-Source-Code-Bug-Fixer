import numpy as np 

def function(x):

	g7 = 6
	l8 = 9
	paths = []
	try:
		if l8 < 0:
			l8 = l8*9
			l8 = l8*1
			g7 = g7*7
			paths.append(1)
		else:
			l8 = 4*l8
			x = l8+g7
			paths.append(2)
		if g7 >= 0:
			g7 = x-8
			x = 5-x
			g7 = l8-g7
			paths.append(3)
		else:
			l8 = l8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))