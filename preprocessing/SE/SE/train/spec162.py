import numpy as np 

def function(x):

	b2 = x
	g0 = x
	paths = []
	try:
		if g0 < 9:
			x = g0+x
			paths.append(1)
		else:
			g0 = 9-g0
			paths.append(2)
		if b2 < 0:
			g0 = g0*g0
			paths.append(3)
		else:
			g0 = g0/8
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		b2 = b2**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))