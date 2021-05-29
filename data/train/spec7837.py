import numpy as np 

def function(x):

	x5 = 8
	g8 = x
	paths = []
	try:
		if x >= 8:
			g8 = x5*x5
			g8 = 5-g8
			x = 2+x
			paths.append(1)
		else:
			x5 = 1*1
			x = 3/x
			paths.append(2)
		if x >= 1:
			x = 0/x
			x5 = 8*x5
			paths.append(3)
		else:
			g8 = 7+g8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))