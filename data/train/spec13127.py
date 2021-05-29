import numpy as np 

def function(x):

	l0 = 9
	g5 = x
	x = 6
	paths = []
	try:
		if g5 >= 3:
			x = 3+l0
			paths.append(1)
		else:
			g5 = 7/g5
			x = x+2
			paths.append(2)
		if g5 > 2:
			x = x/2
			l0 = 0+l0
			paths.append(3)
		else:
			l0 = l0/3
			l0 = l0/l0
			g5 = l0/g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))