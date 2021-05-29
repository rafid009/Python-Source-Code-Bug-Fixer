import numpy as np 

def function(x):

	l4 = x
	g0 = x
	paths = []
	try:
		if x > 5:
			l4 = g0/l4
			paths.append(1)
		else:
			x = x+l4
			paths.append(2)
		if g0 <= 8:
			g0 = 1*g0
			paths.append(3)
		else:
			g0 = 5-l4
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))