import numpy as np 

def function(x):

	v9 = x
	g6 = 6
	paths = []
	try:
		if x < 8:
			g6 = g6*3
			v9 = v9/x
			paths.append(1)
		else:
			v9 = 9*v9
			x = 0+x
			g6 = 4-9
			paths.append(2)
		if x >= 4:
			x = 5*9
			x = g6/7
			v9 = 8/v9
			paths.append(3)
		else:
			x = g6*x
			g6 = g6-3
			x = 1/g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		v9 = g6**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))