import numpy as np 

def function(x):

	g3 = x
	l2 = 4
	paths = []
	try:
		if l2 > 7:
			g3 = 4*g3
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if l2 >= 0:
			g3 = 9/g3
			g3 = g3+x
			paths.append(3)
		else:
			l2 = l2+l2
			g3 = g3+2
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))