import numpy as np 

def function(x):

	a6 = x
	g8 = x
	paths = []
	try:
		if a6 >= 9:
			g8 = 9*9
			x = x*2
			x = 6*3
			paths.append(1)
		else:
			x = x/4
			a6 = x+2
			paths.append(2)
		if a6 >= 8:
			a6 = a6/9
			g8 = a6/3
			paths.append(3)
		else:
			g8 = g8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))