import numpy as np 

def function(x):

	g5 = x
	n3 = 1
	paths = []
	try:
		if g5 > 3:
			x = 3/3
			n3 = n3*8
			paths.append(1)
		else:
			x = g5-9
			n3 = n3-8
			paths.append(2)
		if g5 < 5:
			g5 = g5*g5
			x = x/x
			n3 = 2*n3
			paths.append(3)
		else:
			n3 = 0-n3
			g5 = 6+g5
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		g5 = n3**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))