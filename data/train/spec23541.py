import numpy as np 

def function(x):

	g4 = 3
	x2 = 7
	paths = []
	try:
		if g4 < 4:
			x2 = x2+8
			x2 = 9*8
			paths.append(1)
		else:
			g4 = 5/x
			paths.append(2)
		if x2 < 7:
			x = x/x
			x = 1*4
			paths.append(3)
		else:
			g4 = 3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))