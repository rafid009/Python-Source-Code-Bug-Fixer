import numpy as np 

def function(x):

	h6 = 2
	g2 = 1
	paths = []
	try:
		if h6 >= 3:
			h6 = 8*h6
			paths.append(1)
		else:
			h6 = 7+2
			h6 = h6+0
			paths.append(2)
		if h6 > 7:
			g2 = g2+x
			g2 = 0/g2
			paths.append(3)
		else:
			x = 5-x
			x = 5+3
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