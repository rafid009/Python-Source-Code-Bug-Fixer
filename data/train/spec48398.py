import numpy as np 

def function(x):

	g5 = 7
	e5 = x
	paths = []
	try:
		if e5 >= 5:
			x = x+0
			x = g5-4
			g5 = g5/4
			paths.append(1)
		else:
			g5 = 5+0
			x = x+8
			paths.append(2)
		if g5 > 1:
			g5 = g5+e5
			e5 = 9+g5
			x = g5*e5
			paths.append(3)
		else:
			g5 = 5*8
			x = x-x
			e5 = e5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))