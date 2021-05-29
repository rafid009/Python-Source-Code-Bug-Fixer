import numpy as np 

def function(x):

	g6 = x
	j3 = x
	paths = []
	try:
		if x >= 9:
			g6 = g6/4
			x = 7-j3
			g6 = g6/8
			paths.append(1)
		else:
			j3 = 2+j3
			paths.append(2)
		if x > 2:
			g6 = g6-j3
			paths.append(3)
		else:
			j3 = j3+j3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		g6 = j3**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))