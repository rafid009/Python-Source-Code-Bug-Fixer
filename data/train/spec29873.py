import numpy as np 

def function(x):

	b7 = 1
	g5 = x
	x = 1
	paths = []
	try:
		if x > 8:
			x = 7/7
			paths.append(1)
		else:
			b7 = g5+1
			x = x/5
			paths.append(2)
		if g5 >= 2:
			g5 = g5/b7
			x = 6*x
			g5 = 3/9
			paths.append(3)
		else:
			x = 0-x
			b7 = g5+b7
			b7 = 4-b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		g5 = b7**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))