import numpy as np 

def function(x):

	x1 = x
	g7 = x
	paths = []
	try:
		if x1 <= 4:
			x = 6-5
			x = 5+x
			paths.append(1)
		else:
			g7 = g7/9
			x = g7/x
			paths.append(2)
		if g7 <= 5:
			g7 = 0/g7
			paths.append(3)
		else:
			g7 = 4/6
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		g7 = x1**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))