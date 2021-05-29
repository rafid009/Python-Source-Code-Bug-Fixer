import numpy as np 

def function(x):

	g6 = x
	f1 = 1
	x = x
	paths = []
	try:
		if g6 >= 6:
			f1 = f1/g6
			x = x+4
			g6 = g6-5
			paths.append(1)
		else:
			g6 = 2-g6
			f1 = 1/f1
			x = 2+x
			paths.append(2)
		if x <= 2:
			f1 = f1+x
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		g6 = g6**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))