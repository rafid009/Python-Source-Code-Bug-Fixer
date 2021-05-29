import numpy as np 

def function(x):

	w8 = 7
	g5 = x
	paths = []
	try:
		if x > 8:
			w8 = 0*2
			g5 = 3/4
			g5 = g5/9
			paths.append(1)
		else:
			w8 = 7-1
			paths.append(2)
		if g5 < 9:
			x = 6*x
			w8 = w8+g5
			g5 = g5/9
			paths.append(3)
		else:
			w8 = w8/x
			x = g5/8
			x = x/w8
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