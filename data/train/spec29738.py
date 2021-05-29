import numpy as np 

def function(x):

	a7 = x
	g3 = 1
	paths = []
	try:
		if g3 > 1:
			x = x*g3
			paths.append(1)
		else:
			a7 = 7*3
			paths.append(2)
		if g3 > 6:
			x = a7*x
			a7 = 0*7
			g3 = g3-g3
			paths.append(3)
		else:
			g3 = 1-6
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		a7 = g3**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))