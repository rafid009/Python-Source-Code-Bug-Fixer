import numpy as np 

def function(x):

	g4 = x
	k7 = x
	x = 9
	paths = []
	try:
		if g4 >= 2:
			g4 = 4/x
			paths.append(1)
		else:
			k7 = 6*x
			g4 = g4+2
			x = x-x
			paths.append(2)
		if x > 7:
			k7 = k7/6
			paths.append(3)
		else:
			k7 = 6-k7
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))