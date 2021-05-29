import numpy as np 

def function(x):

	w3 = x
	g0 = 3
	paths = []
	try:
		if g0 <= 3:
			w3 = w3+7
			paths.append(1)
		else:
			g0 = g0+x
			x = x/7
			paths.append(2)
		if x < 8:
			x = w3-0
			g0 = 0-x
			x = x-2
			paths.append(3)
		else:
			x = x-8
			w3 = 3*w3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))