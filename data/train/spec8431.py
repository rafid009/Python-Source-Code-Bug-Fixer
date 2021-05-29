import numpy as np 

def function(x):

	f9 = x
	g7 = 9
	paths = []
	try:
		if g7 >= 3:
			g7 = 0-7
			f9 = 7-6
			f9 = f9+5
			paths.append(1)
		else:
			f9 = g7*3
			paths.append(2)
		if x > 6:
			x = 6-3
			f9 = f9+f9
			paths.append(3)
		else:
			f9 = 2+f9
			f9 = f9*g7
			x = x*1
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		g7 = g7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))