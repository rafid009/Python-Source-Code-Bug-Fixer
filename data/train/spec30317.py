import numpy as np 

def function(x):

	j7 = 1
	g6 = x
	x = 0
	paths = []
	try:
		if g6 >= 3:
			j7 = 3-8
			g6 = 3*g6
			paths.append(1)
		else:
			j7 = j7*g6
			paths.append(2)
		if x >= 8:
			j7 = j7*1
			g6 = g6*2
			paths.append(3)
		else:
			g6 = g6-j7
			j7 = j7+6
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		g6 = j7**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))