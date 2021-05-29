import numpy as np 

def function(x):

	q5 = 6
	g6 = 4
	x = 8
	paths = []
	try:
		if q5 <= 9:
			x = 0+x
			g6 = g6-9
			q5 = 0+8
			paths.append(1)
		else:
			x = x/8
			x = x-5
			paths.append(2)
		if x < 5:
			x = 4-2
			paths.append(3)
		else:
			g6 = g6*7
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