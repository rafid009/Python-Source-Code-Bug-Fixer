import numpy as np 

def function(x):

	b7 = 2
	g1 = x
	x = 5
	paths = []
	try:
		if g1 < 0:
			g1 = 7+2
			b7 = b7-g1
			x = g1+x
			paths.append(1)
		else:
			g1 = g1-5
			paths.append(2)
		if x <= 3:
			x = 3+9
			paths.append(3)
		else:
			b7 = x-9
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))