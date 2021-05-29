import numpy as np 

def function(x):

	m0 = x
	g8 = 7
	x = x
	paths = []
	try:
		if g8 <= 8:
			g8 = g8+m0
			x = m0+g8
			g8 = 1+g8
			paths.append(1)
		else:
			x = x+3
			g8 = m0-g8
			paths.append(2)
		if m0 >= 0:
			g8 = g8+4
			paths.append(3)
		else:
			x = 1+4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))