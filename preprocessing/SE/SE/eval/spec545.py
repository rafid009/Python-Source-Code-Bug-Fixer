import numpy as np 

def function(x):

	b5 = x
	g6 = x
	paths = []
	try:
		if x < 1:
			g6 = 0+g6
			x = x-g6
			paths.append(1)
		else:
			x = 2*x
			paths.append(2)
		if x > 9:
			b5 = 4*b5
			b5 = b5-3
			g6 = g6*1
			paths.append(3)
		else:
			b5 = g6+b5
			x = 5+7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		g6 = b5**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))