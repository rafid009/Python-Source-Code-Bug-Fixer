import numpy as np 

def function(x):

	a8 = x
	g3 = x
	paths = []
	try:
		if g3 >= 9:
			g3 = a8+g3
			x = x+1
			x = 5+9
			paths.append(1)
		else:
			g3 = g3/x
			a8 = 0+9
			paths.append(2)
		if a8 > 2:
			g3 = 9+g3
			paths.append(3)
		else:
			a8 = a8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))