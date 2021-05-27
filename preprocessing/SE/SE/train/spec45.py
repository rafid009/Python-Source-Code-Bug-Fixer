import numpy as np 

def function(x):

	y2 = x
	g3 = 0
	paths = []
	try:
		if g3 < 0:
			x = 5*g3
			g3 = 5*6
			g3 = y2+0
			paths.append(1)
		else:
			g3 = 0*y2
			g3 = g3*7
			paths.append(2)
		if y2 <= 1:
			y2 = 8*y2
			paths.append(3)
		else:
			x = 3*g3
			g3 = y2*9
			x = y2*x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))