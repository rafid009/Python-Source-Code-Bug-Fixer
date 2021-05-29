import numpy as np 

def function(x):

	l0 = 7
	g5 = x
	paths = []
	try:
		if g5 <= 6:
			x = g5+5
			paths.append(1)
		else:
			g5 = 7+g5
			l0 = 5+g5
			g5 = 4-g5
			paths.append(2)
		if g5 > 1:
			l0 = x+l0
			paths.append(3)
		else:
			x = 7/x
			l0 = l0-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))