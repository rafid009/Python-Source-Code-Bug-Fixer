import numpy as np 

def function(x):

	u3 = 7
	g7 = x
	paths = []
	try:
		if g7 < 1:
			g7 = g7*9
			g7 = x*g7
			x = 5/x
			paths.append(1)
		else:
			u3 = 8*g7
			g7 = 8-g7
			u3 = u3/3
			paths.append(2)
		if x > 4:
			u3 = u3/3
			u3 = 5/u3
			paths.append(3)
		else:
			g7 = g7-7
			x = x*1
			g7 = 9+0
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