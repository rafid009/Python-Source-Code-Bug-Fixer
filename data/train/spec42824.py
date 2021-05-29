import numpy as np 

def function(x):

	y8 = 9
	g4 = x
	paths = []
	try:
		if g4 > 8:
			y8 = 1+9
			g4 = g4-y8
			paths.append(1)
		else:
			y8 = 8-2
			g4 = 8-g4
			paths.append(2)
		if x <= 9:
			x = x+3
			paths.append(3)
		else:
			x = 3*6
			x = x+x
			y8 = y8+5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))