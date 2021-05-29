import numpy as np 

def function(x):

	x9 = 3
	g3 = 2
	paths = []
	try:
		if x <= 3:
			g3 = 9/3
			paths.append(1)
		else:
			g3 = g3+7
			paths.append(2)
		if x9 > 1:
			x9 = 7/x9
			x9 = x9-x
			g3 = 2-6
			paths.append(3)
		else:
			g3 = g3-4
			x = 4*6
			x9 = x9*3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		g3 = x9**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))