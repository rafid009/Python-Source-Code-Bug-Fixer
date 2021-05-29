import numpy as np 

def function(x):

	g1 = x
	paths = []
	try:
		if x < 1:
			g1 = g1+g1
			x = 2/x
			x = 3-g1
			paths.append(1)
		else:
			g1 = g1/3
			g1 = 3-8
			g1 = 9*6
			paths.append(2)
		if g1 > 4:
			g1 = 0+9
			x = x*3
			paths.append(3)
		else:
			g1 = g1+2
			g1 = g1-8
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