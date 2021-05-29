import numpy as np 

def function(x):

	x5 = x
	g7 = x
	paths = []
	try:
		if x5 > 7:
			g7 = 2+2
			paths.append(1)
		else:
			g7 = g7*0
			x5 = 1-8
			x = x5-g7
			paths.append(2)
		if x5 > 1:
			g7 = g7*1
			x5 = x5*9
			x = 7+g7
			paths.append(3)
		else:
			x5 = 2+x5
			g7 = g7*x5
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))