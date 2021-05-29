import numpy as np 

def function(x):

	w6 = x
	g5 = x
	paths = []
	try:
		if x >= 8:
			g5 = 1-0
			g5 = 2/g5
			paths.append(1)
		else:
			x = 3/x
			w6 = w6+5
			paths.append(2)
		if x >= 2:
			w6 = w6-3
			x = 8*w6
			paths.append(3)
		else:
			x = x/x
			x = 6-8
			w6 = x+w6
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))