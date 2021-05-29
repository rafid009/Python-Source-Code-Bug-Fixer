import numpy as np 

def function(x):

	a8 = x
	g3 = x
	paths = []
	try:
		if x >= 2:
			a8 = g3+2
			g3 = g3/2
			paths.append(1)
		else:
			x = 9+x
			x = 6+x
			g3 = g3+4
			paths.append(2)
		if x >= 8:
			g3 = 9/g3
			paths.append(3)
		else:
			x = 7-a8
			a8 = a8-2
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))