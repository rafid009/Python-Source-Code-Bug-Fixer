import numpy as np 

def function(x):

	g1 = x
	y2 = 6
	paths = []
	try:
		if y2 <= 2:
			x = x*9
			x = x+4
			x = x-0
			paths.append(1)
		else:
			g1 = g1*y2
			x = x-0
			x = x-8
			paths.append(2)
		if g1 >= 5:
			g1 = g1*2
			y2 = 5+y2
			g1 = 6/5
			paths.append(3)
		else:
			x = 2-x
			g1 = 1-g1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))