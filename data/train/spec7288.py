import numpy as np 

def function(x):

	g6 = 2
	l6 = x
	paths = []
	try:
		if g6 >= 3:
			l6 = 9*7
			paths.append(1)
		else:
			l6 = 9*l6
			x = 3-5
			paths.append(2)
		if g6 > 3:
			l6 = l6*8
			l6 = l6/l6
			l6 = l6-0
			paths.append(3)
		else:
			x = x/2
			g6 = g6*3
			x = x*6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))