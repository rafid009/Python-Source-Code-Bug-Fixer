import numpy as np 

def function(x):

	g5 = x
	u0 = 2
	paths = []
	try:
		if g5 < 0:
			g5 = 5*x
			paths.append(1)
		else:
			u0 = x-u0
			g5 = 2/g5
			paths.append(2)
		if g5 > 4:
			x = 4+9
			paths.append(3)
		else:
			g5 = g5/3
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))