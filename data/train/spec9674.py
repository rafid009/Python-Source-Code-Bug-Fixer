import numpy as np 

def function(x):

	g1 = 5
	l7 = x
	paths = []
	try:
		if x <= 2:
			x = 8+x
			l7 = l7+g1
			l7 = l7-6
			paths.append(1)
		else:
			l7 = 7*l7
			paths.append(2)
		if x >= 8:
			l7 = l7/9
			paths.append(3)
		else:
			l7 = 8-g1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))