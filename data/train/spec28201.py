import numpy as np 

def function(x):

	g7 = x
	f0 = 5
	x = x
	paths = []
	try:
		if x < 2:
			x = f0+x
			f0 = f0/4
			paths.append(1)
		else:
			f0 = g7*8
			paths.append(2)
		if f0 >= 6:
			f0 = 9*g7
			paths.append(3)
		else:
			x = 1*8
			g7 = g7+g7
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		x = g7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))