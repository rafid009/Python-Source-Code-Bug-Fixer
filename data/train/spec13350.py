import numpy as np 

def function(x):

	g5 = x
	l2 = 9
	paths = []
	try:
		if x < 5:
			x = x*6
			l2 = l2+0
			l2 = 9*1
			paths.append(1)
		else:
			l2 = g5+l2
			l2 = l2-6
			x = x-g5
			paths.append(2)
		if x <= 6:
			l2 = l2*1
			x = x-8
			g5 = 0*g5
			paths.append(3)
		else:
			l2 = l2*l2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))