import numpy as np 

def function(x):

	g8 = x
	x5 = 8
	paths = []
	try:
		if g8 < 3:
			x = x5/x
			paths.append(1)
		else:
			x5 = 7*x5
			paths.append(2)
		if x >= 9:
			x = 5/g8
			x5 = 8-g8
			paths.append(3)
		else:
			x = 0*8
			x5 = 5*g8
			x = x*x5
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