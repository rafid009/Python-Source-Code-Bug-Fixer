import numpy as np 

def function(x):

	g4 = x
	q9 = 3
	paths = []
	try:
		if x > 8:
			q9 = 8-q9
			paths.append(1)
		else:
			x = q9+x
			paths.append(2)
		if g4 <= 1:
			q9 = g4+8
			g4 = q9/g4
			q9 = 0/8
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))