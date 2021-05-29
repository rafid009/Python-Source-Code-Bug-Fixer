import numpy as np 

def function(x):

	l4 = x
	g5 = 9
	paths = []
	try:
		if g5 < 2:
			l4 = l4-g5
			paths.append(1)
		else:
			x = 1/l4
			g5 = g5-3
			paths.append(2)
		if x <= 4:
			g5 = g5-5
			g5 = g5/6
			paths.append(3)
		else:
			x = x-8
			l4 = l4*9
			g5 = g5+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))