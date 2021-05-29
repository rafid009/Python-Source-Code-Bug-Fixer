import numpy as np 

def function(x):

	g9 = 9
	p6 = x
	paths = []
	try:
		if g9 >= 6:
			g9 = p6-g9
			g9 = x+p6
			x = 3*x
			paths.append(1)
		else:
			g9 = 0/g9
			x = 8-3
			paths.append(2)
		if x >= 1:
			g9 = g9+x
			x = x-9
			paths.append(3)
		else:
			g9 = g9-9
			p6 = x+p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))