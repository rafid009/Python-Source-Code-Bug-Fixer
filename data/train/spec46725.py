import numpy as np 

def function(x):

	g1 = x
	d8 = x
	paths = []
	try:
		if x > 6:
			d8 = 2*9
			g1 = g1-x
			paths.append(1)
		else:
			g1 = 8+x
			paths.append(2)
		if g1 >= 9:
			d8 = 2-d8
			d8 = 2+8
			g1 = 2-x
			paths.append(3)
		else:
			d8 = 4+2
			d8 = d8-x
			g1 = g1+g1
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		g1 = d8**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))