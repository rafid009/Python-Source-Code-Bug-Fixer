import numpy as np 

def function(x):

	o2 = 8
	g6 = x
	paths = []
	try:
		if o2 < 7:
			o2 = 1-g6
			g6 = 0*8
			paths.append(1)
		else:
			o2 = o2-7
			paths.append(2)
		if x >= 4:
			x = x+g6
			paths.append(3)
		else:
			g6 = g6/3
			o2 = x+o2
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))