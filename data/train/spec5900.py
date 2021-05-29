import numpy as np 

def function(x):

	g9 = x
	w8 = 6
	paths = []
	try:
		if x < 2:
			w8 = w8-7
			paths.append(1)
		else:
			g9 = 6*w8
			x = x+x
			paths.append(2)
		if g9 < 9:
			x = x+9
			w8 = w8-6
			g9 = 9/6
			paths.append(3)
		else:
			w8 = w8-9
			w8 = 0+w8
			w8 = 2/g9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))