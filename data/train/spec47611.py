import numpy as np 

def function(x):

	g1 = x
	b1 = x
	paths = []
	try:
		if b1 > 8:
			g1 = g1/b1
			g1 = g1/x
			x = 1-x
			paths.append(1)
		else:
			x = 3+x
			b1 = b1-x
			b1 = 7-x
			paths.append(2)
		if x <= 3:
			g1 = 0-g1
			paths.append(3)
		else:
			x = 9+5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b1 = b1**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))