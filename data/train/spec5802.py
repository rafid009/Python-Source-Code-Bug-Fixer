import numpy as np 

def function(x):

	h4 = x
	g5 = 3
	paths = []
	try:
		if h4 <= 4:
			g5 = g5/8
			h4 = 2-h4
			g5 = h4*g5
			paths.append(1)
		else:
			h4 = h4*h4
			paths.append(2)
		if x < 4:
			g5 = 2+3
			g5 = 5-x
			g5 = 4*8
			paths.append(3)
		else:
			g5 = g5-9
			h4 = 5*h4
			x = x*3
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