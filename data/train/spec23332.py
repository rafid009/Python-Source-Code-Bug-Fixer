import numpy as np 

def function(x):

	a0 = 0
	g6 = x
	paths = []
	try:
		if x < 1:
			g6 = 1/g6
			g6 = g6/5
			paths.append(1)
		else:
			a0 = 8-a0
			g6 = 6/g6
			paths.append(2)
		if a0 < 8:
			g6 = g6+g6
			a0 = 2/x
			a0 = g6+a0
			paths.append(3)
		else:
			a0 = a0*g6
			g6 = g6-7
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))