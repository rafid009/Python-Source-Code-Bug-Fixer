import numpy as np 

def function(x):

	h4 = x
	g5 = x
	paths = []
	try:
		if g5 < 2:
			x = x*3
			h4 = h4+h4
			paths.append(1)
		else:
			h4 = h4*h4
			paths.append(2)
		if x < 7:
			h4 = h4-g5
			x = 9+x
			paths.append(3)
		else:
			x = h4+9
			g5 = 8/5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		h4 = g5**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))