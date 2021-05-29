import numpy as np 

def function(x):

	g6 = 2
	a5 = x
	paths = []
	try:
		if g6 >= 4:
			g6 = g6/a5
			x = 9-x
			g6 = 7/x
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if g6 > 4:
			a5 = 9-a5
			paths.append(3)
		else:
			g6 = 4/g6
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))