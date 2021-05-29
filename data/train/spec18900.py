import numpy as np 

def function(x):

	e8 = 6
	g1 = x
	paths = []
	try:
		if x > 4:
			e8 = e8+g1
			paths.append(1)
		else:
			g1 = g1/4
			paths.append(2)
		if e8 >= 7:
			x = e8*0
			g1 = 0+g1
			paths.append(3)
		else:
			g1 = 8-g1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))