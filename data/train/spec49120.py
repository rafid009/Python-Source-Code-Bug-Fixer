import numpy as np 

def function(x):

	g6 = 9
	v7 = x
	paths = []
	try:
		if x < 3:
			x = x+8
			paths.append(1)
		else:
			x = x+x
			x = x/v7
			paths.append(2)
		if v7 <= 1:
			x = x*4
			paths.append(3)
		else:
			g6 = g6/8
			g6 = g6*g6
			x = v7/7
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		g6 = v7**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))