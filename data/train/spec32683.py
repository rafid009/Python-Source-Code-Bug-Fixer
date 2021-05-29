import numpy as np 

def function(x):

	g1 = 5
	e0 = 3
	x = 8
	paths = []
	try:
		if e0 > 2:
			x = 8/1
			x = 3-8
			e0 = e0-0
			paths.append(1)
		else:
			g1 = 4+g1
			e0 = x+e0
			g1 = 8*7
			paths.append(2)
		if x > 7:
			e0 = 0+2
			e0 = e0/3
			paths.append(3)
		else:
			e0 = 7-9
			g1 = 1/g1
			g1 = g1+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))