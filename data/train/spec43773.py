import numpy as np 

def function(x):

	g6 = x
	x0 = x
	x = 8
	paths = []
	try:
		if x0 > 6:
			x = 0/5
			paths.append(1)
		else:
			x = x*9
			g6 = x+g6
			paths.append(2)
		if g6 > 4:
			g6 = x0*8
			paths.append(3)
		else:
			x0 = 2-x0
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))