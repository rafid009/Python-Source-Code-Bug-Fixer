import numpy as np 

def function(x):

	l7 = 9
	g1 = 4
	paths = []
	try:
		if l7 < 5:
			x = x+x
			g1 = g1*7
			x = 2-x
			paths.append(1)
		else:
			g1 = x*g1
			x = x-l7
			l7 = 2+l7
			paths.append(2)
		if l7 <= 9:
			g1 = 5-g1
			l7 = l7-g1
			paths.append(3)
		else:
			x = x-8
			g1 = g1+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))