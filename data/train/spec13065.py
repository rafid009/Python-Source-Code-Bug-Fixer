import numpy as np 

def function(x):

	g1 = 6
	y0 = 3
	paths = []
	try:
		if g1 >= 3:
			x = x+7
			paths.append(1)
		else:
			x = x-8
			g1 = g1+2
			x = 0/x
			paths.append(2)
		if x > 0:
			g1 = 9/g1
			paths.append(3)
		else:
			g1 = 3-g1
			x = 8+6
			x = g1+3
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))