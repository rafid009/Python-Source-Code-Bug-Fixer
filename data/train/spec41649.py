import numpy as np 

def function(x):

	g7 = x
	e1 = x
	paths = []
	try:
		if g7 >= 4:
			x = e1+7
			paths.append(1)
		else:
			e1 = e1*e1
			paths.append(2)
		if g7 >= 0:
			e1 = e1-7
			paths.append(3)
		else:
			x = 0-4
			e1 = e1/4
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))