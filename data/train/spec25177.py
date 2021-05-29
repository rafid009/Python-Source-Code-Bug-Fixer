import numpy as np 

def function(x):

	g8 = 2
	v1 = 4
	paths = []
	try:
		if v1 < 4:
			g8 = g8/1
			paths.append(1)
		else:
			v1 = g8*3
			g8 = x-x
			v1 = g8/3
			paths.append(2)
		if g8 >= 7:
			x = x*x
			g8 = g8/6
			v1 = 3+0
			paths.append(3)
		else:
			x = 5*x
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