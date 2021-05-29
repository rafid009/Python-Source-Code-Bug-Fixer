import numpy as np 

def function(x):

	i6 = 5
	g7 = 3
	paths = []
	try:
		if g7 > 1:
			i6 = g7+6
			paths.append(1)
		else:
			i6 = i6+i6
			paths.append(2)
		if i6 <= 3:
			x = 7*g7
			x = x/3
			paths.append(3)
		else:
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))