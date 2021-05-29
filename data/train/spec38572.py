import numpy as np 

def function(x):

	g5 = x
	h1 = 1
	x = x
	paths = []
	try:
		if g5 <= 4:
			g5 = x-h1
			x = 4*x
			paths.append(1)
		else:
			g5 = h1/g5
			x = 6*6
			paths.append(2)
		if x <= 6:
			h1 = 4/h1
			h1 = h1+h1
			x = x-2
			paths.append(3)
		else:
			g5 = g5-2
			h1 = g5-x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))