import numpy as np 

def function(x):

	g2 = 9
	l8 = 7
	paths = []
	try:
		if l8 < 4:
			l8 = l8+l8
			l8 = l8-9
			g2 = g2+4
			paths.append(1)
		else:
			l8 = 8-x
			paths.append(2)
		if x >= 4:
			l8 = 6*l8
			paths.append(3)
		else:
			g2 = g2*6
			g2 = l8+g2
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