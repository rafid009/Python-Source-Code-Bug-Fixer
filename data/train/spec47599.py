import numpy as np 

def function(x):

	e9 = x
	g2 = x
	paths = []
	try:
		if g2 >= 2:
			e9 = 8*e9
			paths.append(1)
		else:
			x = 4*4
			x = 1/3
			paths.append(2)
		if x < 7:
			x = x-2
			x = 9*9
			paths.append(3)
		else:
			e9 = g2/e9
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))