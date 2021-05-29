import numpy as np 

def function(x):

	l2 = x
	g4 = x
	paths = []
	try:
		if x >= 5:
			l2 = l2+l2
			paths.append(1)
		else:
			l2 = 8-0
			x = x-4
			g4 = 3/g4
			paths.append(2)
		if g4 > 1:
			l2 = l2/8
			l2 = 2*l2
			x = x/2
			paths.append(3)
		else:
			g4 = 0-4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		l2 = g4**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))