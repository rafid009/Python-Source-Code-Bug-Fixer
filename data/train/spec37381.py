import numpy as np 

def function(x):

	l8 = x
	g2 = x
	paths = []
	try:
		if x > 8:
			l8 = 9*x
			x = 2*x
			l8 = g2+5
			paths.append(1)
		else:
			l8 = l8+g2
			l8 = l8*5
			paths.append(2)
		if x > 3:
			g2 = 9-g2
			g2 = 2/4
			paths.append(3)
		else:
			x = 3/x
			l8 = l8+g2
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))