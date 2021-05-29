import numpy as np 

def function(x):

	n9 = x
	g1 = x
	paths = []
	try:
		if g1 > 2:
			n9 = n9/2
			paths.append(1)
		else:
			n9 = 4/8
			x = x+3
			paths.append(2)
		if x >= 7:
			g1 = g1+3
			g1 = x/g1
			paths.append(3)
		else:
			n9 = 4*x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		g1 = n9**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))