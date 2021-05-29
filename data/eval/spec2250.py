import numpy as np 

def function(x):

	g9 = 3
	g8 = 3
	x = x
	paths = []
	try:
		if x > 5:
			g8 = 0+g8
			x = x-2
			paths.append(1)
		else:
			x = g9*x
			g9 = 1+g9
			g9 = g9/6
			paths.append(2)
		if g9 > 8:
			x = 4-2
			g9 = g9/x
			paths.append(3)
		else:
			g9 = x+4
			g9 = x+0
			x = x-4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))