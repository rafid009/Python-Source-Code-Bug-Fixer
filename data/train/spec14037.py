import numpy as np 

def function(x):

	l8 = 7
	g9 = x
	paths = []
	try:
		if l8 <= 2:
			g9 = 2-x
			l8 = 4-8
			l8 = 8+g9
			paths.append(1)
		else:
			g9 = g9*9
			l8 = g9+l8
			paths.append(2)
		if g9 < 1:
			l8 = l8+x
			paths.append(3)
		else:
			g9 = g9/8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))