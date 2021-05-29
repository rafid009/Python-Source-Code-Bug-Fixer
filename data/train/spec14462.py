import numpy as np 

def function(x):

	g7 = 2
	h1 = x
	x = x
	paths = []
	try:
		if h1 <= 4:
			h1 = h1/2
			g7 = g7-g7
			g7 = x*x
			paths.append(1)
		else:
			g7 = x/1
			x = h1*3
			paths.append(2)
		if g7 < 9:
			g7 = g7/7
			paths.append(3)
		else:
			h1 = g7+x
			x = h1*h1
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		h1 = h1**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))