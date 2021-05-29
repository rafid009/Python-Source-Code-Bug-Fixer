import numpy as np 

def function(x):

	g6 = x
	l2 = 5
	paths = []
	try:
		if l2 <= 3:
			x = 3+x
			x = g6/g6
			g6 = x+g6
			paths.append(1)
		else:
			l2 = l2+7
			g6 = x/5
			l2 = 6/g6
			paths.append(2)
		if x >= 6:
			g6 = g6/l2
			g6 = g6+9
			x = 2+x
			paths.append(3)
		else:
			x = g6+x
			g6 = g6*l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		g6 = l2**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))