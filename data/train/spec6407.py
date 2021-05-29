import numpy as np 

def function(x):

	f5 = 9
	g7 = x
	paths = []
	try:
		if f5 > 0:
			f5 = f5-f5
			paths.append(1)
		else:
			f5 = 0+f5
			paths.append(2)
		if f5 < 3:
			g7 = x/g7
			f5 = 5-g7
			x = x/g7
			paths.append(3)
		else:
			x = x-x
			g7 = 7+f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))