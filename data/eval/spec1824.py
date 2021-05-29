import numpy as np 

def function(x):

	g1 = x
	w9 = 8
	paths = []
	try:
		if w9 > 1:
			w9 = w9-w9
			g1 = 4*7
			x = x/9
			paths.append(1)
		else:
			g1 = g1-2
			w9 = g1*4
			paths.append(2)
		if x > 3:
			x = x/g1
			w9 = 7*g1
			g1 = 2/g1
			paths.append(3)
		else:
			w9 = 5+g1
			w9 = 3+7
			g1 = 2+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))