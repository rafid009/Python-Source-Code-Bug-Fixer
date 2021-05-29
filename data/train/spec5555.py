import numpy as np 

def function(x):

	h8 = x
	g2 = x
	paths = []
	try:
		if g2 > 8:
			g2 = 8-g2
			paths.append(1)
		else:
			x = x*9
			x = h8-6
			g2 = 1+g2
			paths.append(2)
		if h8 > 6:
			x = 0+3
			paths.append(3)
		else:
			h8 = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))