import numpy as np 

def function(x):

	e7 = x
	g4 = x
	paths = []
	try:
		if e7 < 2:
			g4 = x*7
			e7 = 8+e7
			g4 = 6-g4
			paths.append(1)
		else:
			e7 = 8*e7
			g4 = g4*g4
			paths.append(2)
		if e7 <= 2:
			g4 = g4-g4
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))