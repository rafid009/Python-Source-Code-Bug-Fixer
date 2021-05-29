import numpy as np 

def function(x):

	g6 = x
	q9 = 9
	paths = []
	try:
		if q9 > 9:
			q9 = q9*7
			q9 = 2/q9
			q9 = q9-6
			paths.append(1)
		else:
			x = x/3
			q9 = q9-0
			paths.append(2)
		if g6 >= 6:
			g6 = g6+9
			paths.append(3)
		else:
			q9 = 6+q9
			g6 = g6-2
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