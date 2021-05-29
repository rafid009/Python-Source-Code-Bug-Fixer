import numpy as np 

def function(x):

	g2 = x
	h3 = x
	paths = []
	try:
		if x >= 5:
			h3 = 1/h3
			x = 7*x
			paths.append(1)
		else:
			x = x/4
			g2 = g2+h3
			paths.append(2)
		if h3 >= 3:
			g2 = g2+4
			h3 = h3+h3
			paths.append(3)
		else:
			x = 8-x
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