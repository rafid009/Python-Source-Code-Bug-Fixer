import numpy as np 

def function(x):

	g2 = x
	h3 = 9
	paths = []
	try:
		if g2 >= 4:
			g2 = h3-g2
			paths.append(1)
		else:
			h3 = 5/h3
			x = 2/x
			g2 = g2*x
			paths.append(2)
		if x < 2:
			h3 = h3+8
			paths.append(3)
		else:
			x = 9/x
			h3 = h3*5
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		h3 = g2**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))