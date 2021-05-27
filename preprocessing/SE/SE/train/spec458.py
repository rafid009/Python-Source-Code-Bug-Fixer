import numpy as np 

def function(x):

	a4 = x
	g1 = x
	paths = []
	try:
		if g1 <= 3:
			a4 = 5*a4
			g1 = g1*g1
			paths.append(1)
		else:
			a4 = a4-9
			a4 = a4*5
			g1 = 1+a4
			paths.append(2)
		if a4 < 2:
			x = x+5
			paths.append(3)
		else:
			a4 = a4*3
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		g1 = a4**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))