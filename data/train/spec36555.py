import numpy as np 

def function(x):

	g3 = 9
	l6 = x
	x = x
	paths = []
	try:
		if g3 > 8:
			g3 = g3-l6
			l6 = l6/5
			g3 = g3+6
			paths.append(1)
		else:
			x = g3-4
			paths.append(2)
		if g3 >= 5:
			x = x-4
			paths.append(3)
		else:
			x = l6-0
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		g3 = l6**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))