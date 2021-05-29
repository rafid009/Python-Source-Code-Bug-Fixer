import numpy as np 

def function(x):

	h7 = x
	g5 = x
	x = 3
	paths = []
	try:
		if x >= 3:
			g5 = g5/3
			x = 9*8
			paths.append(1)
		else:
			h7 = h7+7
			paths.append(2)
		if g5 >= 8:
			x = x/1
			x = 7+x
			paths.append(3)
		else:
			x = x/3
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		h7 = g5**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))