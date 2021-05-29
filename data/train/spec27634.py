import numpy as np 

def function(x):

	d1 = x
	g4 = 8
	paths = []
	try:
		if g4 >= 7:
			x = x-0
			g4 = g4+x
			g4 = g4+g4
			paths.append(1)
		else:
			d1 = d1/3
			paths.append(2)
		if d1 <= 8:
			x = 9/1
			g4 = d1-g4
			d1 = d1/3
			paths.append(3)
		else:
			g4 = 1-7
			g4 = g4/g4
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		g4 = d1**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))