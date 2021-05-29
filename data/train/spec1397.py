import numpy as np 

def function(x):

	x5 = x
	g4 = 9
	paths = []
	try:
		if g4 >= 8:
			g4 = g4-8
			paths.append(1)
		else:
			g4 = 1+8
			paths.append(2)
		if x5 >= 9:
			g4 = g4+x5
			x = x5+x
			g4 = g4*0
			paths.append(3)
		else:
			x = x*8
			x = 9*x
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x = x5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))