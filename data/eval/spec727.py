import numpy as np 

def function(x):

	g2 = x
	h8 = 6
	x = 2
	paths = []
	try:
		if g2 >= 2:
			g2 = h8/g2
			paths.append(1)
		else:
			h8 = 8+g2
			paths.append(2)
		if g2 > 7:
			x = x*x
			g2 = 1/g2
			paths.append(3)
		else:
			h8 = h8*h8
			x = 3+x
			h8 = 2+h8
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))