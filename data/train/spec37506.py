import numpy as np 

def function(x):

	g7 = x
	r5 = 8
	paths = []
	try:
		if r5 < 1:
			r5 = x+2
			r5 = r5*2
			g7 = g7/g7
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if r5 > 3:
			g7 = g7*6
			paths.append(3)
		else:
			r5 = r5+1
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