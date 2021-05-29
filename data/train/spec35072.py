import numpy as np 

def function(x):

	w9 = x
	g4 = x
	paths = []
	try:
		if g4 <= 9:
			g4 = 9*2
			g4 = 3*x
			paths.append(1)
		else:
			g4 = g4+2
			w9 = 4*w9
			paths.append(2)
		if g4 > 2:
			g4 = 9*9
			w9 = g4+w9
			w9 = w9+w9
			paths.append(3)
		else:
			g4 = g4-6
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))