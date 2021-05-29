import numpy as np 

def function(x):

	x8 = 3
	g4 = x
	paths = []
	try:
		if g4 >= 3:
			x = x/7
			paths.append(1)
		else:
			x8 = 5+x
			x = 7+x8
			paths.append(2)
		if x8 > 6:
			g4 = g4+2
			x = 6*x
			paths.append(3)
		else:
			g4 = x8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))