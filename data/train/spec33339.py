import numpy as np 

def function(x):

	g8 = x
	g9 = 7
	x = x
	paths = []
	try:
		if g9 < 6:
			g8 = g8/6
			g9 = g9-6
			g8 = g8+x
			paths.append(1)
		else:
			g9 = g9/x
			g9 = 6/g9
			paths.append(2)
		if x > 4:
			g9 = x*5
			x = x/1
			paths.append(3)
		else:
			g8 = g9+g8
			g8 = 9+g9
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