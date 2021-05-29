import numpy as np 

def function(x):

	g0 = 8
	w9 = x
	paths = []
	try:
		if g0 > 1:
			w9 = w9*g0
			x = 6*x
			paths.append(1)
		else:
			w9 = w9+1
			paths.append(2)
		if x < 8:
			x = 3+x
			paths.append(3)
		else:
			x = 8-w9
			g0 = 4/g0
			w9 = 3+w9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		g0 = w9**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))