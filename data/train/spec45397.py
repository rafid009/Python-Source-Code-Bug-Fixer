import numpy as np 

def function(x):

	e7 = 8
	g3 = x
	paths = []
	try:
		if x < 8:
			e7 = g3+g3
			e7 = 4*e7
			g3 = g3-4
			paths.append(1)
		else:
			g3 = g3-7
			e7 = 2*7
			e7 = 9+x
			paths.append(2)
		if g3 <= 0:
			g3 = g3/x
			g3 = g3-7
			paths.append(3)
		else:
			g3 = g3*1
			e7 = 7/e7
			g3 = e7+g3
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))