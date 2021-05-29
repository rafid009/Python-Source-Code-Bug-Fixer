import numpy as np 

def function(x):

	x5 = x
	g3 = 4
	paths = []
	try:
		if x >= 2:
			x = 2*g3
			paths.append(1)
		else:
			x = g3/x
			g3 = x5/8
			paths.append(2)
		if x5 >= 5:
			g3 = g3+9
			paths.append(3)
		else:
			x5 = 4-x5
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))