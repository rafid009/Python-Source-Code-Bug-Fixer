import numpy as np 

def function(x):

	g6 = 4
	w9 = 9
	paths = []
	try:
		if w9 <= 1:
			w9 = 6*4
			g6 = 3-g6
			x = 5-w9
			paths.append(1)
		else:
			w9 = w9-x
			x = x*3
			x = x-7
			paths.append(2)
		if x > 9:
			w9 = 0*w9
			x = 1*w9
			paths.append(3)
		else:
			w9 = 1*1
			w9 = 6*x
			g6 = x-g6
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		g6 = w9**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))