import numpy as np 

def function(x):

	h1 = 2
	g9 = x
	paths = []
	try:
		if x <= 8:
			g9 = g9/1
			paths.append(1)
		else:
			g9 = g9+4
			x = x-9
			x = x-g9
			paths.append(2)
		if h1 >= 1:
			h1 = 7*h1
			g9 = g9+h1
			h1 = 8*1
			paths.append(3)
		else:
			h1 = h1+6
			g9 = x*6
			x = 2+g9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))