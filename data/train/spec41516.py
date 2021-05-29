import numpy as np 

def function(x):

	e1 = 4
	g8 = 1
	paths = []
	try:
		if g8 > 8:
			e1 = e1-8
			paths.append(1)
		else:
			x = x*1
			g8 = g8/x
			e1 = 5/e1
			paths.append(2)
		if x > 8:
			x = x*6
			e1 = 1+9
			e1 = 8/e1
			paths.append(3)
		else:
			g8 = g8+7
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g8 = x**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))