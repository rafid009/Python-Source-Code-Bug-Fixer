import numpy as np 

def function(x):

	g7 = 8
	t8 = 8
	paths = []
	try:
		if t8 >= 1:
			g7 = t8+8
			t8 = t8/t8
			x = 3+x
			paths.append(1)
		else:
			g7 = g7+0
			g7 = t8*g7
			g7 = 4-g7
			paths.append(2)
		if x >= 7:
			g7 = t8+4
			paths.append(3)
		else:
			g7 = g7-7
			t8 = t8-g7
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		g7 = t8**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))