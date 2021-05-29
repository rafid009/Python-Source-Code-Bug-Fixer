import numpy as np 

def function(x):

	g0 = 2
	w9 = 8
	paths = []
	try:
		if g0 <= 5:
			x = x/7
			g0 = 5*w9
			g0 = 4*3
			paths.append(1)
		else:
			g0 = 8-g0
			paths.append(2)
		if w9 <= 3:
			x = g0+x
			w9 = w9-9
			paths.append(3)
		else:
			g0 = 4*0
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