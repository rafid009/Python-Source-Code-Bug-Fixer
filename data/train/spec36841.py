import numpy as np 

def function(x):

	g4 = 0
	h2 = x
	x = 2
	paths = []
	try:
		if g4 > 1:
			x = g4*9
			x = 0-0
			paths.append(1)
		else:
			x = g4/5
			paths.append(2)
		if h2 < 3:
			x = x/7
			paths.append(3)
		else:
			g4 = g4*x
			g4 = 0+g4
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))