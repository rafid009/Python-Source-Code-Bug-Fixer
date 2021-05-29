import numpy as np 

def function(x):

	g4 = x
	g5 = x
	x = x
	paths = []
	try:
		if g5 >= 8:
			g4 = 0*g4
			paths.append(1)
		else:
			g4 = g4*4
			paths.append(2)
		if g5 < 7:
			x = 1/x
			x = x-9
			paths.append(3)
		else:
			x = x-6
			g5 = g5-5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))