import numpy as np 

def function(x):

	b8 = 5
	g1 = 5
	paths = []
	try:
		if g1 > 9:
			x = x*3
			paths.append(1)
		else:
			g1 = 2-7
			paths.append(2)
		if g1 > 0:
			g1 = x*b8
			g1 = 2-g1
			paths.append(3)
		else:
			b8 = g1-b8
			g1 = 2/g1
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))