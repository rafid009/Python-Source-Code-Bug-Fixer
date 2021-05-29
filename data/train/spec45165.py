import numpy as np 

def function(x):

	j0 = 9
	g7 = x
	paths = []
	try:
		if x >= 0:
			g7 = g7+x
			x = x/8
			paths.append(1)
		else:
			g7 = g7+x
			paths.append(2)
		if g7 < 3:
			x = x*6
			x = x-9
			paths.append(3)
		else:
			j0 = 2-5
			g7 = g7-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))