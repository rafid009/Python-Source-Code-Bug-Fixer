import numpy as np 

def function(x):

	l5 = x
	g3 = 9
	paths = []
	try:
		if l5 > 8:
			l5 = 3/2
			paths.append(1)
		else:
			g3 = l5/4
			g3 = g3/4
			paths.append(2)
		if l5 < 1:
			g3 = 1/5
			g3 = g3+l5
			paths.append(3)
		else:
			l5 = 9*x
			g3 = 0-4
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		l5 = g3**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))