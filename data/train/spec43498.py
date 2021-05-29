import numpy as np 

def function(x):

	q7 = x
	g4 = 2
	paths = []
	try:
		if q7 < 5:
			g4 = g4-q7
			paths.append(1)
		else:
			x = x-7
			q7 = 6+q7
			q7 = q7-q7
			paths.append(2)
		if g4 > 3:
			x = 1-x
			g4 = g4-7
			paths.append(3)
		else:
			g4 = q7+6
			x = 8/9
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		g4 = q7**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))