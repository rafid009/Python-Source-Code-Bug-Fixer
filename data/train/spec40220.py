import numpy as np 

def function(x):

	g7 = 5
	e5 = x
	paths = []
	try:
		if x < 1:
			g7 = g7*2
			x = x/2
			g7 = 4-g7
			paths.append(1)
		else:
			x = x/5
			g7 = g7*6
			paths.append(2)
		if x <= 9:
			x = 4+9
			paths.append(3)
		else:
			e5 = e5+0
			g7 = g7-7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		e5 = g7**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))