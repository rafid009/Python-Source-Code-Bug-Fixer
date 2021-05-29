import numpy as np 

def function(x):

	d8 = 2
	g1 = x
	x = 9
	paths = []
	try:
		if x >= 0:
			x = 9/d8
			x = x*9
			paths.append(1)
		else:
			g1 = 3*8
			x = x-5
			paths.append(2)
		if g1 > 9:
			x = x+x
			paths.append(3)
		else:
			d8 = d8-4
			d8 = d8*6
			d8 = d8-g1
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