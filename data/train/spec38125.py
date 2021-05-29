import numpy as np 

def function(x):

	l4 = x
	g1 = 9
	paths = []
	try:
		if x > 1:
			g1 = g1*x
			g1 = l4-1
			paths.append(1)
		else:
			l4 = 5*l4
			paths.append(2)
		if l4 < 3:
			g1 = 4*g1
			g1 = l4-9
			paths.append(3)
		else:
			l4 = 1-7
			x = 0/3
			x = 4+g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))