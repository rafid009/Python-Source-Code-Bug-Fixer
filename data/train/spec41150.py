import numpy as np 

def function(x):

	t2 = x
	g8 = x
	paths = []
	try:
		if t2 > 3:
			g8 = 0+x
			paths.append(1)
		else:
			g8 = x+3
			paths.append(2)
		if g8 > 3:
			t2 = t2/x
			g8 = x+g8
			paths.append(3)
		else:
			g8 = g8/6
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))