import numpy as np 

def function(x):

	g8 = x
	g9 = x
	paths = []
	try:
		if x > 4:
			g8 = g9*g8
			g9 = 2+8
			g8 = g8/3
			paths.append(1)
		else:
			g9 = 0*g9
			x = 1/8
			paths.append(2)
		if g8 <= 7:
			x = x*4
			g8 = x-2
			g9 = g9*9
			paths.append(3)
		else:
			g8 = 6-4
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g9 = g8**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))