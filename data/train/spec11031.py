import numpy as np 

def function(x):

	g9 = x
	l2 = x
	x = 5
	paths = []
	try:
		if l2 >= 1:
			g9 = g9-l2
			x = x+9
			x = 3+x
			paths.append(1)
		else:
			x = 5*l2
			paths.append(2)
		if x <= 1:
			g9 = g9+x
			paths.append(3)
		else:
			g9 = 9-g9
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		g9 = l2**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))