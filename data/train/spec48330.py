import numpy as np 

def function(x):

	g9 = x
	y7 = 5
	paths = []
	try:
		if y7 > 2:
			g9 = g9-5
			y7 = y7-8
			paths.append(1)
		else:
			x = 4+0
			g9 = g9*9
			paths.append(2)
		if x >= 6:
			g9 = g9/9
			x = x+x
			x = 0*x
			paths.append(3)
		else:
			g9 = g9/1
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