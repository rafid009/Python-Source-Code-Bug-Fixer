import numpy as np 

def function(x):

	g7 = 2
	n2 = 3
	paths = []
	try:
		if g7 <= 1:
			g7 = 2/g7
			g7 = g7+5
			paths.append(1)
		else:
			n2 = 0+x
			g7 = g7-0
			paths.append(2)
		if n2 < 0:
			g7 = x/g7
			g7 = 4-g7
			g7 = 4/9
			paths.append(3)
		else:
			g7 = g7*0
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		g7 = n2**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))