import numpy as np 

def function(x):

	g3 = x
	f3 = x
	paths = []
	try:
		if x >= 9:
			f3 = f3/g3
			paths.append(1)
		else:
			f3 = 8-f3
			x = 3/8
			g3 = 7*x
			paths.append(2)
		if x > 8:
			g3 = f3-6
			g3 = g3*4
			paths.append(3)
		else:
			f3 = 2*g3
			x = x*f3
			g3 = 9*f3
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))