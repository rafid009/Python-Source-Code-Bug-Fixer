import numpy as np 

def function(x):

	g5 = x
	q6 = x
	paths = []
	try:
		if x >= 6:
			g5 = g5/g5
			x = g5-7
			paths.append(1)
		else:
			x = 5-x
			g5 = g5/8
			g5 = 1+3
			paths.append(2)
		if g5 > 9:
			g5 = x*5
			q6 = 5-7
			paths.append(3)
		else:
			q6 = 6-1
			g5 = g5/1
			g5 = g5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))