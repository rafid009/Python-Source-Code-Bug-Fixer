import numpy as np 

def function(x):

	g3 = x
	n9 = 3
	paths = []
	try:
		if x > 8:
			g3 = 8*g3
			paths.append(1)
		else:
			x = 6*x
			x = g3/5
			paths.append(2)
		if x >= 0:
			g3 = 8*2
			paths.append(3)
		else:
			n9 = n9/3
			g3 = n9/x
			g3 = g3+x
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