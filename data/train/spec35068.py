import numpy as np 

def function(x):

	a0 = 0
	g3 = x
	paths = []
	try:
		if g3 >= 4:
			g3 = g3/x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if a0 < 9:
			a0 = a0+x
			paths.append(3)
		else:
			x = x-g3
			g3 = 3+a0
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		a0 = g3**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))