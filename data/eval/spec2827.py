import numpy as np 

def function(x):

	t7 = x
	g7 = 1
	paths = []
	try:
		if g7 < 7:
			g7 = x*g7
			g7 = 0-g7
			paths.append(1)
		else:
			x = 6-8
			g7 = g7+g7
			x = x-g7
			paths.append(2)
		if g7 > 8:
			g7 = g7*x
			x = 9/3
			x = 9+x
			paths.append(3)
		else:
			t7 = t7*x
			x = x/t7
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