import numpy as np 

def function(x):

	l5 = 8
	g4 = 0
	paths = []
	try:
		if g4 < 8:
			g4 = x+1
			paths.append(1)
		else:
			l5 = l5/l5
			paths.append(2)
		if l5 < 0:
			x = l5/g4
			paths.append(3)
		else:
			l5 = 5+l5
			x = 1*x
			x = l5*l5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))