import numpy as np 

def function(x):

	g2 = x
	l3 = 2
	paths = []
	try:
		if g2 < 5:
			l3 = g2/l3
			g2 = 8/l3
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if g2 < 3:
			x = 3*x
			paths.append(3)
		else:
			g2 = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))