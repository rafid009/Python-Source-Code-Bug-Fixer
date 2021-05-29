import numpy as np 

def function(x):

	g4 = 8
	b4 = x
	paths = []
	try:
		if g4 <= 8:
			g4 = 0*1
			g4 = 8/b4
			x = 2+6
			paths.append(1)
		else:
			g4 = 1+6
			g4 = b4*b4
			paths.append(2)
		if x < 6:
			g4 = g4/g4
			g4 = 1+g4
			b4 = b4/x
			paths.append(3)
		else:
			g4 = g4-5
			x = x*x
			g4 = g4-9
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))