import numpy as np 

def function(x):

	g0 = x
	p2 = 3
	paths = []
	try:
		if x >= 0:
			g0 = g0-5
			paths.append(1)
		else:
			g0 = 1-8
			paths.append(2)
		if g0 <= 4:
			x = x+2
			p2 = x-p2
			g0 = g0-9
			paths.append(3)
		else:
			x = 5-2
			x = g0/p2
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		x = g0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))