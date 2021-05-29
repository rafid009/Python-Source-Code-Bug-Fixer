import numpy as np 

def function(x):

	y3 = 6
	g4 = 3
	x = x
	paths = []
	try:
		if y3 <= 4:
			g4 = g4+y3
			paths.append(1)
		else:
			y3 = 0+y3
			g4 = 2/g4
			y3 = y3-5
			paths.append(2)
		if y3 < 2:
			g4 = g4-9
			g4 = g4*x
			paths.append(3)
		else:
			g4 = 2*g4
			x = x-x
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))