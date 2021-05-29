import numpy as np 

def function(x):

	l7 = 8
	g1 = x
	paths = []
	try:
		if x >= 9:
			g1 = g1/2
			paths.append(1)
		else:
			x = l7/4
			paths.append(2)
		if x >= 4:
			x = x+l7
			l7 = 6-l7
			g1 = x-4
			paths.append(3)
		else:
			l7 = 7*l7
			g1 = g1*l7
			l7 = l7/l7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		l7 = g1**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))