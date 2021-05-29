import numpy as np 

def function(x):

	g1 = 8
	l7 = 6
	paths = []
	try:
		if x >= 5:
			l7 = 6+l7
			g1 = 6-g1
			paths.append(1)
		else:
			l7 = g1*g1
			paths.append(2)
		if x <= 4:
			g1 = g1*x
			x = x+1
			paths.append(3)
		else:
			g1 = l7+g1
			x = 7*x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))