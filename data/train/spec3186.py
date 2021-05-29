import numpy as np 

def function(x):

	g4 = 7
	d6 = x
	paths = []
	try:
		if g4 < 9:
			d6 = d6*x
			paths.append(1)
		else:
			x = x+d6
			paths.append(2)
		if d6 >= 9:
			d6 = 1-d6
			g4 = x-g4
			paths.append(3)
		else:
			d6 = 8-0
			d6 = g4-1
			d6 = d6*7
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