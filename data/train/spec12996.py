import numpy as np 

def function(x):

	a2 = 2
	g1 = x
	paths = []
	try:
		if g1 <= 4:
			g1 = 5*g1
			paths.append(1)
		else:
			g1 = 0-a2
			a2 = x-g1
			g1 = 2+9
			paths.append(2)
		if g1 < 2:
			g1 = g1-g1
			x = x/6
			paths.append(3)
		else:
			g1 = 6+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))