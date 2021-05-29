import numpy as np 

def function(x):

	j9 = x
	g6 = 6
	paths = []
	try:
		if x > 4:
			g6 = 8*7
			g6 = g6-g6
			paths.append(1)
		else:
			j9 = 7*j9
			j9 = 3-j9
			paths.append(2)
		if g6 >= 2:
			j9 = j9-1
			g6 = g6-9
			paths.append(3)
		else:
			j9 = j9/3
			j9 = 4-0
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))