import numpy as np 

def function(x):

	g4 = 9
	l2 = x
	x = x
	paths = []
	try:
		if l2 < 6:
			g4 = g4/g4
			g4 = 6/6
			paths.append(1)
		else:
			l2 = 6*x
			paths.append(2)
		if g4 < 8:
			l2 = g4+l2
			x = x*1
			paths.append(3)
		else:
			l2 = 7-l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))