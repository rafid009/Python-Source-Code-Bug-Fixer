import numpy as np 

def function(x):

	l3 = 2
	g8 = x
	paths = []
	try:
		if x < 1:
			g8 = g8*g8
			l3 = l3+6
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if l3 > 3:
			x = x/5
			x = 7-x
			g8 = g8-2
			paths.append(3)
		else:
			x = l3/x
			g8 = l3+g8
			g8 = g8+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))