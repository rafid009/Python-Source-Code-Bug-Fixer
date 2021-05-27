import numpy as np 

def function(x):

	g7 = x
	j1 = x
	paths = []
	try:
		if x > 5:
			g7 = g7/2
			x = 6/j1
			j1 = g7*3
			paths.append(1)
		else:
			j1 = 4*0
			j1 = 2+j1
			paths.append(2)
		if x <= 6:
			g7 = g7-j1
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))