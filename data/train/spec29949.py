import numpy as np 

def function(x):

	e0 = 6
	g5 = x
	x = x
	paths = []
	try:
		if e0 >= 6:
			g5 = g5+x
			paths.append(1)
		else:
			x = 6+g5
			e0 = e0-0
			paths.append(2)
		if x < 1:
			e0 = e0-1
			paths.append(3)
		else:
			x = g5*3
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))