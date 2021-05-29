import numpy as np 

def function(x):

	f2 = 9
	g7 = x
	paths = []
	try:
		if x <= 9:
			x = g7*5
			x = 5*x
			f2 = f2*x
			paths.append(1)
		else:
			f2 = f2+f2
			paths.append(2)
		if g7 >= 9:
			x = 2+x
			f2 = f2+4
			f2 = 4+9
			paths.append(3)
		else:
			g7 = 6*x
			g7 = x+9
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))