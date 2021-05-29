import numpy as np 

def function(x):

	g9 = x
	h8 = 2
	paths = []
	try:
		if x > 0:
			g9 = g9+7
			paths.append(1)
		else:
			g9 = g9+g9
			h8 = 5+h8
			paths.append(2)
		if h8 <= 8:
			g9 = g9+5
			x = x+2
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		h8 = g9**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))