import numpy as np 

def function(x):

	a9 = x
	g3 = 0
	x = 2
	paths = []
	try:
		if g3 > 2:
			a9 = a9+2
			g3 = 2*6
			a9 = 3-a9
			paths.append(1)
		else:
			g3 = a9-g3
			paths.append(2)
		if g3 > 4:
			x = x+2
			x = 1-a9
			paths.append(3)
		else:
			x = x-6
			g3 = x+g3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))