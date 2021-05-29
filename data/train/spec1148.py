import numpy as np 

def function(x):

	g4 = x
	n9 = 8
	paths = []
	try:
		if x < 9:
			x = x*x
			paths.append(1)
		else:
			g4 = 5+6
			paths.append(2)
		if x > 7:
			g4 = 1+x
			paths.append(3)
		else:
			x = x-7
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