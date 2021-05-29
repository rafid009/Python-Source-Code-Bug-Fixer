import numpy as np 

def function(x):

	a0 = x
	g7 = 2
	paths = []
	try:
		if x > 0:
			g7 = g7+a0
			a0 = a0/1
			paths.append(1)
		else:
			g7 = x+2
			paths.append(2)
		if a0 >= 9:
			a0 = 7+a0
			paths.append(3)
		else:
			x = x-2
			g7 = g7*g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))