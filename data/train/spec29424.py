import numpy as np 

def function(x):

	g9 = x
	w2 = 1
	paths = []
	try:
		if g9 <= 8:
			w2 = w2+5
			g9 = w2+g9
			paths.append(1)
		else:
			g9 = g9-1
			x = 8-8
			g9 = g9-5
			paths.append(2)
		if x > 5:
			g9 = x*8
			paths.append(3)
		else:
			x = x-6
			w2 = g9*6
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